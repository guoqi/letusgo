#!/usr/bin/python
#coding: utf-8
class BaseConfig(object):
    '''Base config'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:a767813944@localhost/letusgo'
    API_KEY = '363f98db9209a9f79de6d431d6b951b4'


class DevelopmentConfig(BaseConfig):
    '''Development mode'''
    DEBUG = True

class ProductConfig(BaseConfig):
    DEBUG = False
