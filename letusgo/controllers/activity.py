#!/usr/bin/python
#coding: utf-8
from flask import Blueprint, request, g
from sqlalchemy import or_
import json
import time
from datetime import datetime

from ..tools import require_login, filter, gettimestamp
from ..models import Activity, db
from ..errors import ThrownError

bp = Blueprint('activity', __name__)

def time_validate(s, e):
    d = time.time()
    if s < e and s > d and e > d:
        return True
    else:
        raise ThrownError('Time illegal.')

@bp.route('/release', methods=['POST'])
@require_login
def release():
    args = g.args
    filter(args, ('name', 'start_t', 'end_t', 'limits', 'longitude', 'latitude'))
    info = args.get('intro', '', type=str)
    image = args.get('image', '', type=str)
    time_validate(args['start_t'], args['end_t'])
    a = Activity(args['name'], g.user.uid, args['start_t'], args['end_t'], \
            args['limits'], args['longitude'], args['latitude'], info, image)
    db.session.add(a)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)

@bp.route('/upload', methods=['POST'])
@require_login
def upload():
    pass

@bp.route('/profile', methods=['POST'])
@require_login
def profile():
    args = g.args
    filter(args, ('aid', 'start_t', 'end_t', 'limits', 'longitude', 'latitude'))
    info = args.get('intro', '', type=str)
    image = args.get('image', '', type=str)
    time_validate(args['start_t'], args['end_t'])
    start_t = datetime.fromtimestamp(float(args['start_t']))
    end_t = datetime.fromtimestamp(float(args['end_t']))
    a = Activity.query.filter(Activity.aid == args['aid']).first()
    if a is None:
        raise ThrownError('No such activity.')
    if a.host != g.user:
        raise ThrownError('You do not have the privilege.')
    for k in args.iterkeys():
        setattr(a, k, args[k])
    a.start_t = start_t
    a.end_t = end_t
    a.intro = info
    a.image = image
    db.session.add(a)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)

@bp.route('/delete', methods=['POST'])
@require_login
def delete():
    args = g.args
    filter(args, ('aid', ))
    a = Activity.query.filter(Activity.aid == args['aid']).first()
    if a is None:
        raise ThrownError('No such activity.')
    if a.host != g.user:
        raise ThrownError('You do not have the privilege.')
    db.session.delete(a) 
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)

@bp.route('/near', methods=['GET'])
def near():
    args = request.args
    filter(args, ('l', 'b'))
    activities = Activity.query.all()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'ActiEvent': []
                }
        }
    for a in activities:
        d = a.distances(float(args['l']), float(args['b']))
        if d <= 1:
            r['result']['ActiEvent'].append(a.dump())
            r['result']['ActiEvent'][-1]['distances'] = d
    return json.dumps(r)

@bp.route('/list', methods=['GET'])
def list():
    args = request.args
    filter(args, ('s', 'l', 'b'))
    activities = Activity.query.order_by(Activity.launch_t.desc()).paginate(int(args['s']), 10, False)
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'ActiEvent':[]
                }
        }
    for a in activities.items:
        d = a.distances(float(args['l']), float(args['b']))
        r['result']['ActiEvent'].append(a.dump())
        r['result']['ActiEvent'][-1]['distances'] = d
    return json.dumps(r)

@bp.route('/search', methods=['GET'])
def search():
    args = request.args
    filter(args, ('q', ))
    activities = Activity.query.filter(or_(Activity.name.like('%'+args['q']+'%'), \
            Activity.intro.like('%'+args['q']+'%'))).all()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'ActiEvent':[]
                }
        }
    for a in activities:
        d = a.distances(float(args['l']), float(args['b']))
        r['result']['ActiEvent'].append(a.dump())
        r['result']['ActiEvent'][-1]['distances'] = d
    return json.dumps(r)

@bp.route('/participants', methods=['GET'])
def participants():
    args = request.args
    filter(args, ('aid', ))
    a = Activity.query.filter(Activity.aid == args['aid']).first()
    if a is None:
        raise ThrownError('No such activity.')
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Actor': []
                }
        }
    for u in a.joins:
        r['result']['Actor'].append(u.dump())
    return json.dumps(r)

@bp.route('/join', methods=['POST'])
@require_login
def join():
    args = g.args
    filter(args, ('aid', ))
    a = Activity.query.filter(Activity.aid == args['aid']).first()
    if a is None:
        raise ThrownError('No such activity.')
    if a in g.user.p_activities:
        g.user.p_activities.remove(a)
        a.participants -= 1
    else:
        g.user.p_activities.append(a)
        a.participants += 1
    db.session.add(g.user)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)
    
@bp.route('/voteup', methods=['POST'])
@require_login
def voteup():
    args = g.args
    filter(args, ('aid', ))
    a = Activity.query.filter(Activity.aid == args['aid']).first()
    if a is None:
        raise ThrownError('No such activity.')
    if a in g.user.v_activities:
        g.user.v_activities.remove(a)
        a.voteups -= 1
    else:
        g.user.v_activities.append(a)
        a.voteups += 1
    db.session.add(g.user)
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)
