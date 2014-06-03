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
    from controllers import account, activity, review
    app.register_blueprint(account.bp, url_prefix='/account')
    app.register_blueprint(activity.bp, url_prefix='/activity')
    app.register_blueprint(review.bp, url_prefix='/review')

def init_errorhandlers(app):
    import json
    from errors import ThrownError, InternalError

    @app.errorhandler(ThrownError)
    def thrownerror(e):
        r = {
                'status': False, 
                'message': e.err, 
                'result': ''
            }
        return json.dumps(r)

    @app.errorhandler(500)
    @app.errorhandler(InternalError)
    def internalerror(e):
        r = {
                'status': False, 
                'message': 'Internal Error', 
                'result': ''
            }
        return json.dumps(r)

    @app.errorhandler(404)
    def notfound(e):
        r = {
                'status': False, 
                'message': 'Not Found', 
                'result': ''
            }
        return json.dumps(r)
    
app = init_app()
