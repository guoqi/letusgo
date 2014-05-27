#!/usr/bin/python
#coding: utf-8
from letusgo.models import db
from letusgo import app

with app.app_context():
    db.drop_all()
    db.create_all()
