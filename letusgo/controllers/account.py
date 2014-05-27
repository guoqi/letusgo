#!/usr/bin/python
#coding: utf-8
from flask import Blueprint, request
import json
import base64

from ..tools import sms, filter, istimeout, hash, gentoken
from ..models import User, db
from ..errors import ThrownError, InternalError

bp = Blueprint('account', __name__)

@bp.route('/login', methods=['POST'])
def login():
    args = request.form
    filter(args, ('tel', 'info', 'dd'))
    user = User.query.filter(User.tel==args.get('tel')).first()
    if user is None:
        raise ThrownError('Wrong telephone number')
    istimeout(args['dd'])
    print user.tel, user.pwd, args['dd']
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
                'User': user.dump()
                }
        }
    return json.dumps(r)

@bp.route('/reg', methods='POST')
def reg():
    args = request.form
    filter(args, ('tel', 'pwd'))

