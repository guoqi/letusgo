#!/usr/bin/python
#coding: utf-8
import os

DEFAULT_PATH_PREFIX = os.getcwd()

AVATAR_DIR = DEFAULT_PATH_PREFIX + os.sep + 'letusgo/avatar'
IMAGE_DIR = DEFAULT_PATH_PREFIX + os.sep + 'letusgo/image'

DEFAULT_AVATAR_CACHE_DIR = AVATAR_DIR + os.sep + 'cache'

DEFAULT_AVATAR_DIR = AVATAR_DIR + os.sep + 'default'
DEFAULT_AVATAR_ORIGIN = DEFAULT_AVATAR_DIR + os.sep + 'default.png'
DEFAULT_AVATAR_BIG = DEFAULT_AVATAR_DIR + os.sep + 'default64.png'
DEFAULT_AVATAR_SMALL = DEFAULT_AVATAR_DIR + os.sep + 'default32.png'


HOST = 'http://www.uniqueguoqi.com:4000'

H_AVATAR_DIR = HOST + '/' + 'img/avatar'
H_IMAGE_DIR = HOST + '/' + 'img/image'

H_DEFAULT_AVATAR_DIR = H_AVATAR_DIR + '/' + 'default'
H_DEFAULT_AVATAR_ORIGIN = H_DEFAULT_AVATAR_DIR + '/' + 'default.png'
H_DEFAULT_AVATAR_BIG = H_DEFAULT_AVATAR_DIR + '/' + 'default64.png'
H_DEFAULT_AVATAR_SMALL = H_DEFAULT_AVATAR_DIR + '/' + 'default32.png'

AVATAR_BIG_SIZE = (128, 128)
AVATAR_SMALL_SIZE = (96, 96)

APP_NAME = 'Let\'s Go!'
COMPANY_NAME = 'Go!'

TIME_OUT = 30

SMS_TPL_REG = 6

PNG_MIMETYPE = 'image/png'

ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'bmp'])
