#!/usr/bin/python
#coding: utf-8
from datetime import datetime

from _base import db
from participant import Participant
from ..errors import ThrownError
from ..globals import DEFAULT_AVATAR_BIG, DEFAULT_AVATAR_SMALL, DEFAULT_AVATAR_ORIGIN

class User(db.Model):
    '''
    User model
    '''
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    tel = db.Column(db.String(11), nullable=False, unique=True)
    pwd = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    big_avatar = db.Column(db.String(255), nullable=False, default=DEFAULT_AVATAR_BIG)
    small_avatar = db.Column(db.String(255), nullable=False, default=DEFAULT_AVATAR_SMALL)
    origin_avatar = db.Column(db.String(255), nullable=False, default=DEFAULT_AVATAR_ORIGIN)
    # sex 
    # 1 indicates male while 0 indicates female.
    sex = db.Column(db.SmallInteger, nullable=False, default=1)
    age = db.Column(db.SmallInteger, nullable=False)
    loc = db.Column(db.String(255), nullable=False)
    reg_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_login_t = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    token = db.Column(db.String(255), nullable=False)

    h_activities = db.relationship('Activity', backref=db.backref('host', lazy='select'), lazy='select')
    p_activities = db.relationship('Activity', backref=db.backref('joins', lazy='select'), lazy='select', secondary=Participant)

    reviews = db.relationship('Review', backref=db.backref('reviewer', lazy='select'), lazy='select')

    def render_avatar(self, type='small'):
        '''
        Return a file object of avatar.
        '''
        pic = {
                'small': self.small_avatar, 
                'big': self.big_avatar, 
                'origin': self.origin_avatar
                }
        if type not in pic.keys():
            raise ThrownError('Avatar type error')
        return open(pic[type], 'rb')


