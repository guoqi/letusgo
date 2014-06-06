#!/usr/bin/python
#coding: utf-8
from datetime import datetime
from sqlalchemy.dialects.mysql import DOUBLE
import math
import time

from _base import db
from ..tools import gettimestamp

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
    # 0 means to do; 1 means doing; 2 means done.
    status = db.Column(db.SmallInteger, nullable=False, default=0)
    limits = db.Column(db.Integer, nullable=False)
    participants = db.Column(db.Integer, nullable=False, default=0)
    voteups = db.Column(db.Integer, nullable=False, default=0)
    longitude = db.Column(DOUBLE, nullable=False)
    latitude = db.Column(DOUBLE, nullable=False)
    loc = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    reviews = db.relationship('Review', backref=db.backref('activity', lazy='select'), lazy='dynamic')

    def __init__(self, name, uid, start_t, end_t, limits, longitude, latitude, loc, intro='', image=''):
        self.name = name
        self.uid = int(uid)
        self.start_t = datetime.fromtimestamp(float(start_t))
        self.end_t = datetime.fromtimestamp(float(end_t))
        self.limits = int(limits)
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.loc = loc
        self.intro = intro
        self.image = image

    def render_image(self):
        return open(self.image, 'rb')

    @property
    def last_time(self):
        '''
        Return what time does this activity last for.
        '''
        return self.end_t - self.start_t

    def convert(self):
        self.longitude = float(self.longitude)
        self.latitude = float(self.latitude)

    def distances(self, l, b):
        '''
        Return distances from a specified location.
        '''
        mlon_a = self.longitude * math.pi / 180
        mlat_a = (90 - self.latitude) * math.pi / 180
        mlon_b = l * math.pi / 180
        mlat_b = (90 - b) * math.pi / 180
        c = math.sin(mlat_a) * math.sin(mlat_b) * math.cos(mlon_a-mlon_b) + math.cos(mlat_a) * math.cos(mlat_b)
        d = 6371.004 * math.acos(c) * math.pi / 180
        return d

    def dump(self):
        '''
        Dump the object.
        '''
        dd = int(math.ceil(time.time()))
        if dd - gettimestamp(self.start_t) > 0:
            if dd < gettimestamp(self.end_t) < 0:
                self.status = 1
            else:
                self.status = 2
        db.session.add(self)
        db.session.commit()
        print self.last_time
        self.convert()
        return {
                    'aid': self.aid, 
                    'name': self.name, 
                    'host': self.host.dump(), 
                    'intro': self.intro, 
                    'launch_t': gettimestamp(self.launch_t), 
                    'start_t': gettimestamp(self.start_t), 
                    'end_t': gettimestamp(self.end_t), 
                    'last_time': self.last_time.total_seconds(),
                    'status': self.status, 
                    'limits': self.limits, 
                    'participants': self.participants, 
                    'voteups': self.voteups, 
                    'longitude': self.longitude, 
                    'latitude': self.latitude, 
                    'loc': self.loc, 
                    'image': self.image 
                }
