#!/usr/bin/python
#coding: utf-8
from datetime import datetime

from _base import db
from participant import Participant
from voteup import Voteup
from ..errors import ThrownError
from ..globals import H_DEFAULT_AVATAR_BIG, H_DEFAULT_AVATAR_SMALL, H_DEFAULT_AVATAR_ORIGIN

class User(db.Model):
    '''
    User model
    '''
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    tel = db.Column(db.String(11), nullable=False, unique=True)
    pwd = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False, default='Anonymous')
    big_avatar = db.Column(db.String(255), nullable=False, default=H_DEFAULT_AVATAR_BIG)
    small_avatar = db.Column(db.String(255), nullable=False, default=H_DEFAULT_AVATAR_SMALL)
    origin_avatar = db.Column(db.String(255), nullable=False, default=H_DEFAULT_AVATAR_ORIGIN)
    # sex 
    # 1 indicates male while 0 indicates female.
    sex = db.Column(db.SmallInteger, nullable=False, default=1)
    age = db.Column(db.SmallInteger, nullable=False, default=0)
    loc = db.Column(db.String(255), nullable=True)
    reg_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_login_t = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    token = db.Column(db.String(16), nullable=False)

    h_activities = db.relationship('Activity', backref=db.backref('host', lazy='select'), lazy='select')
    p_activities = db.relationship('Activity', backref=db.backref('joins', lazy='select'), lazy='select', secondary=Participant)
    v_activities = db.relationship('Activity', backref=db.backref('voters', lazy='select'), lazy='select', secondary=Voteup)

    reviews = db.relationship('Review', backref=db.backref('reviewer', lazy='select'), lazy='select')


    def __init__(self, tel, pwd, token):
        self.tel = tel
        self.pwd = pwd
        self.token = token

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

    def dump(self):
        return {
                'uid': self.uid, 
                'tel': self.tel, 
                'name': self.name,
                'big_avatar': self.big_avatar, 
                'small_avatar': self.small_avatar, 
                'sex': self.sex, 
                'age': self.age, 
                'loc': self.loc
                }

