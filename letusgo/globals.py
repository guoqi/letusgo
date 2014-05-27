#!/usr/bin/python
#coding: utf-8
import os

DEFAULT_PATH_PREFIX = os.getcwd()

AVATAR_DIR = DEFAULT_PATH_PREFIX + os.sep + 'letusgo/avatar'

DEFAULT_AVATAR_DIR = AVATAR_DIR + os.sep + 'letusgo/avatar/default'
DEFAULT_AVATAR_ORIGIN = DEFAULT_AVATAR_DIR + os.sep + 'default.png'
DEFAULT_AVATAR_BIG = DEFAULT_AVATAR_DIR + os.sep + 'default64.png'
DEFAULT_AVATAR_SMALL = DEFAULT_AVATAR_DIR + os.sep + 'default32.png'
DEFAULT_AVATAR_CACHE_DIR = DEFAULT_AVATAR_DIR + os.sep + 'cache'

AVATAR_BIG_SIZE = (64, 64)
AVATAR_SMALL_SIZE = (32, 32)

APP_NAME = 'Let\'s Go!'
COMPANY_NAME = 'Go!'

TIME_OUT = 30
