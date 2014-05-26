#!/usr/bin/python
#coding: utf-8
from datetime import datetime

from _base import db

class Activity(db.Model):
    '''
    Activity Model
    '''
    aid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    # you can use Activity.host to visit the host of this activity
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)

    intro = db.Column(db.String(255), nullable=False)
    launch_t = db.Column(db.DateTime, nullable=False, default=datetime.now())
    update_t = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    start_t = db.Column(db.DateTime, nullable=False)
    end_t = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    limits = db.Column(db.Integer, nullable=False)
    participants = db.Column(db.Integer, nullable=False, default=0)
    voteups = db.Column(db.Integer, nullable=False, default=0)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)

    reviews = db.relationship('Review', backref=db.backref('activity', lazy='select'), lazy='dynamic')

    def render_image(self):
        return open(self.image, 'rb')

    @property
    def last_time(self):
        '''
        Return what time does this activity last for.
        '''
        return self.end_t - self.start_t

