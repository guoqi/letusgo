#!/usr/bin/python
#coding: utf-8
from _base import db
from ..errors import ThrownError

class User(db.Model):
    '''
    User model
    '''
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    tel = db.Column(db.String(11), nullable=False)
    pwd = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    big_avatar = db.Column(db.String(255), nullable=False)
    small_avatar = db.Column(db.String(255), nullable=False)
    origin_avatar = db.Column(db.String(255, nullable=False))
    sex = db.Column(db.SmallInteger, nullable=False)
    age = db.Column(db.SmallInteger, nullable=False)
    loc = db.Column(db.String(255), nullable=False)
    reg_time = db.Column(db.DateTime, nullable=False)
    last_login_t = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(255), nullable=False)

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


