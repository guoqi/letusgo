#!/usr/bin/python
#coding: utf-8
class BaseConfig(object):
    '''Base config'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:a767813944@localhost/ideashare'


class DevelopmentConfig(BaseConfig):
    '''Development mode'''
    DEBUG = True

class ProductConfig(BaseConfig):
    DEBUG = False
