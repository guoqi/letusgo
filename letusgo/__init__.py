#!/usr/bin/python
#coding: utf-8
from flask import Flask

from .config import DevelopmentConfig

def init_app():
    '''
    init the app
    return an object of Flask
    '''
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    return app


app = init_app()
