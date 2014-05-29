#!/usr/bin/python
#coding: utf-8
from flask import Blueprint, request, g
import json

from ..tools import require_login
from ..models import Review, db
# from ..errors import ThrownError

bp = Blueprint('review', __name__)

@bp.route('/list', methods=['GET'])
def list():
    args = request.args
    filter(args, ('aid', 's'))
    reviews = Review.query.order_by(Review.review_t.desc()).paginate(args['s'], 10, False)
    r = {
            'status': True, 
            'message': 'OK', 
            'result': {
                'Review': []
                }
        }
    for rev in reviews:
        r['result']['Review'].append(rev.dump())
    return json.dumps(r)

@bp.route('/release', methods=['POST'])
@require_login
def release():
    args = request.form
    filter(args, ('aid', 'content'))
    r = Review(content=args['content'], aid=args['aid'], uid=g.user.uid)
    db.session.add(r) 
    db.session.commit()
    r = {
            'status': True, 
            'message': 'OK', 
            'result': ''
        }
    return json.dumps(r)