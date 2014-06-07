#!/usr/bin/python
#coding: utf-8
from flask import Blueprint, request, g
import json

from ..tools import require_login, filter
from ..models import Review, db
# from ..errors import ThrownError

bp = Blueprint('review', __name__)

@bp.route('/list', methods=['GET'])
def list():
    args = request.args
    print args
    filter(args, ('aid', 's'))
    reviews = Review.query.order_by(Review.review_t.desc()).paginate(int(args['s']), 10, False)
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Comment': []
                }
        }
    for rev in reviews:
        r['result']['Comment'].append(rev.dump())
    return json.dumps(r)

@bp.route('/release', methods=['POST'])
@require_login
def release():
    args = g.args
    print args
    filter(args, ('aid', 'content'))
    r = Review(content=args['content'], aid=int(args['aid']), uid=g.user.uid)
    db.session.add(r) 
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)
