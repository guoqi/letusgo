#!/usr/bin/python
#coding: utf-8

class InternalError(Exception):
    '''
    Internal server error.
    This type of errors must be logged and return it's value.
    '''
    def __init__(self, err, message):
        self.err = err
        self.message = message

class ThrownError(Exception):
    '''
    Error which can be thrown directly indicates it isn\'t so emergent.
    '''
    def __init__(self, err):
        self.err = err
