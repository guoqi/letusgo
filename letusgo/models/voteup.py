#!/usr/bin/python
#coding: utf-8
from _base import db

'''
Voteup Model
'''
Voteup = db.Table('voteup', 
        db.Column('aid', db.Integer, db.ForeignKey('activity.aid'), nullable=False), 
        db.Column('uid', db.Integer, db.ForeignKey('user.uid'), nullable=False)
    )
