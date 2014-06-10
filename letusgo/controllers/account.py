#!/usr/bin/python
#coding: utf-8
from flask import Blueprint, request, g
import json
import base64
import shelve
import time
import os
from werkzeug import secure_filename

from ..tools import sms, filter, istimeout, hash, gentoken, gencaptcha, require_login, \
        thumbnails, convert2png, allowed_file
from ..models import User, db
from ..errors import ThrownError, InternalError
from ..globals import AVATAR_DIR

bp = Blueprint('account', __name__)

@bp.route('/login', methods=['POST'])
def login():
    args = request.form
    filter(args, ('tel', 'info', 'dd'))
    user = User.query.filter(User.tel==args.get('tel')).first()
    if user is None:
        raise ThrownError('Wrong telephone number')
    istimeout(args['dd'])
    # print user.tel, user.pwd, args['dd']
    print args['tel'], args['info'], args['dd'], type(args['tel']), type(args['info']), type(args['dd'])
    print hash(':'.join([user.tel, user.pwd, args['dd']])), args['info']
    if hash(':'.join([user.tel, user.pwd, args['dd']])) != args['info']:
        raise ThrownError('Wrong password')
    # login success, genrate token and return
    user.token = gentoken()
    db.session.add(user)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Actor': user.dump()
                }
            }
    r['result']['Actor']['token'] = user.token
    return json.dumps(r)

@bp.route('/reg', methods=['POST'])
def reg():
    args = request.form
    filter(args, ('tel', 'pwd'))
    pwd = base64.decodestring(args['pwd'])
    u = User.query.filter(User.tel == args['tel']).first()
    if u is not None:
        raise ThrownError('Phone has been used.')
    d = shelve.open('temp')
    d['tel'] = args['tel']
    d['pwd'] = hash(pwd)
    d['captcha'] = gencaptcha()
    d['dd'] = time.time()
    # send short message
    sms.tpl_send(d['tel'], d['captcha'])
    # close storage
    d.close()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
            }
    return json.dumps(r)

@bp.route('/verify', methods=['POST'])
def verify():
    args = request.form
    filter(args, ('v', 'dd'))
    istimeout(args['dd'])

    # fetch the storage
    d = shelve.open('temp')
    # filter the storage
    filter(d, ('tel', 'pwd', 'captcha', 'dd'))
    istimeout(d['dd'], 300)
    if hash(':'.join([d['captcha'], args['dd']])) != args['v']:
        raise ThrownError('Wrong captcha.')
    u = User(d['tel'], d['pwd'], gentoken())
    db.session.add(u)
    db.session.commit()
    d.clear()
    d.close()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Actor': u.dump()
            }
        }
    r['result']['Actor']['token'] = u.token
    return json.dumps(r)

@bp.route('/profile', methods=['POST'])
@require_login
def profile():
    filter(g.args, ('name', 'avatar', 'sex', 'age', 'loc'))
    for k in g.args.iterkeys():
        setattr(g.user, k, g.args[k])
    db.session.add(g.user)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Actor': g.user.dump()
                }
        }
    return json.dumps(r)

@bp.route('/pwd', methods=['POST'])
@require_login
def pwd():
    filter(g.args, ('new_pwd', ))
    print g.args['new_pwd']
    g.user.pwd = hash(base64.decodestring(g.args['new_pwd']))
    print g.user.pwd
    db.session.add(g.user)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
            }
    return json.dumps(r)

@bp.route('/avatar', methods=['POST'])
@require_login
def avatar():
    file = request.files['avatar']
    if not file:
        raise ThrownError('Not file.')
    f, e = allowed_file(file.filename)
    path = os.sep.join([AVATAR_DIR, 'cache', g.user.id+e])
    file.save(path)
    convert2png(path)
    d = thumbnails(g.user.id, g.user.id)
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'big_avatar': d['url'][1], 
                'small_avatar': d['url'][2]
            }
        }
    return json.dumps(r)

@bp.route('/info', methods=['GET'])
def info():
    args = request.args
    filter(args, ('uid', ))
    u = User.query.filter(User.uid == args['uid']).first()
    if u is None:
        raise ThrownError('Not such user')
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Actor': u.dump()
                }
            }
    r['result']['Actor']['h_activities'] = []
    r['result']['Actor']['p_activities'] = []
    for a in u.h_activities:
        r['result']['Actor']['h_activities'].append(a.dump())
    for a in u.p_activities:
        r['result']['Actor']['p_activities'].append(a.dump())
    return json.dumps(r)

