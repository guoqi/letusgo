#!/usr/bin/python
#coding: utf-8
from flask import Flask

from .config import DevelopmentConfig

def init_app():
    '''
    Initialize the app
    return an object of Flask
    '''
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    init_db(app)
    return app

def init_db(app):
    '''
    Initialize the datebase.
    '''
    from models import db
    db.init_app(app)
    
app = init_app()
