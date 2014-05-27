#!/usr/bin/python
#coding: utf-8
from flask import Flask

from config import DevelopmentConfig

def init_app():
    '''
    Initialize the app
    return an object of Flask
    '''
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    init_db(app)
    init_sms(app)
    init_blueprint(app)
    init_errorhandlers(app)
    return app

def init_db(app):
    '''
    Initialize the datebase.
    '''
    from models import db
    db.init_app(app)

def init_sms(app):
    '''
    Initialize sms sender
    '''
    from tools import sms
    sms.init_app(app)

def init_blueprint(app):
    '''
    Initialize blueprints
    '''
    from controllers import account
    app.register_blueprint(account.bp, url_prefix='/account')

def init_errorhandlers(app):
    import json
    from errors import ThrownError

    @app.errorhandler(ThrownError)
    def handle(e):
        r = {
                'status': False, 
                'message': e.err, 
                'result': ''
                }
        return json.dumps(r)
    
app = init_app()
