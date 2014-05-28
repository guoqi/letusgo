#!/usr/bin/python
#coding: utf-8
from datetime import datetime

from _base import db

class Review(db.Model):
    rid = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.String(65535), nullable=False)
    # use review.activity
    aid = db.Column(db.Integer, db.ForeignKey('activity.aid'), nullable=False)
    # use review.reviewer
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    review_t = db.Column(db.DateTime, nullable=False, default=datetime.now())
     
    def dump(self):
        '''
        Dump the object.
        '''
        return {
                'rid': self.rid, 
                'content': self.content, 
                'reviewer': self.reivewer.dump()
                }
