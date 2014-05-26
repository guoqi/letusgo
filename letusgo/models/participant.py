#!/usr/bin/python
#coding: utf-8
from _base import db

'''
Participant Model
'''
Participant = db.Table('participant', 
        db.Column('aid', db.Integer, db.ForeignKey('activity.aid')), 
        db.Column('uid', db.Integer, db.ForeignKey('user.uid')) 
    )
