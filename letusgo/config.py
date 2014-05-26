#!/usr/bin/python
#coding: utf-8
class BaseConfig(object):
    '''Base config'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:a767813944@localhost/letusgo'


class DevelopmentConfig(BaseConfig):
    '''Development mode'''
    DEBUG = True

class ProductConfig(BaseConfig):
    DEBUG = False
