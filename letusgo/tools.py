#!/usr/bin/python
#coding: utf-8
from PIL import Image
import md5
import os
import json
import urllib
import urllib2
import thread
import random
import string
import time
from datetime import datetime

from globals import AVATAR_DIR, AVATAR_BIG_SIZE, AVATAR_SMALL_SIZE, DEFAULT_AVATAR_CACHE_DIR, \
        APP_NAME, COMPANY_NAME, TIME_OUT, SMS_TPL_REG
from errors import InternalError, ThrownError

def hash(string):
    return md5.md5(string).hexdigest()

def gettimestamp(dd):
    if isinstance(dd, datetime):
        return int(time.mktime(dd.timetuple()))
    else:
        raise InternalError('Type Error', 'Only datetime object can convert to timestamp')

def gentoken():
    '''
    Genrate a token.
    '''
    src = string.ascii_letters + string.digits
    seq = []
    for i in range(16):
        seq.append(random.choice(src))
    random.shuffle(seq)
    return ''.join(seq)

def gencaptcha():
    '''
    Genrate a captcha.
    '''
    seq = []
    for i in range(6):
        seq.append(random.choice(string.digits))
    random.shuffle(seq)
    return ''.join(seq)

def genpath(*args):
    return os.sep.join(args)

def filter(d, t):
    '''
    Filter parameters which are essential.
    '''
    for i in t:
        if not d.has_key(i):
            raise ThrownError('Wrong Parameters')
    return True

def istimeout(dd, timeout=TIME_OUT):
    '''
    Return whether the request is timeout or not.
    '''
    print dd, gettimestamp(datetime.now())
    diff  = int(gettimestamp(datetime.now())) - int(dd)
    print diff
    if diff < 0 or diff > timeout:
        raise ThrownError('Time out')
    return True

def thumbnails(image_dir, filename='default'):
    '''
    Genrate a thumbnail of user\'s avatar.
    Return a tuble include origin picture\'s path, 64*64 thumbnail\'s path and 32*32 thumbnail\'s path.
    '''
    inputfile = genpath(DEFAULT_AVATAR_CACHE_DIR, filename+'.png')
    outputdir= genpath(AVATAR_DIR, image_dir)
    if not os.path.isfile(inputfile):
        raise InternalError('File not found', 'File {path} does\'t exist'.format(path=inputfile))
    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)
    try:
        img = Image.open(inputfile)
        o = genpath(outputdir, filename+'.png')
        img.save(o, 'PNG')
        img.thumbnail(AVATAR_BIG_SIZE)
        o64 = genpath(outputdir, filename+'64.png')
        img.save(o64, 'PNG')
        img.thumbnail(AVATAR_SMALL_SIZE)
        o32 = genpath(outputdir, filename+'32.png')
        img.save(o32, 'PNG')
    except IOError as e:
        raise InternalError('File io error', e.message)
    # remove cache file
    os.remove(inputfile)
    return (o, o64, o32)

def convert2png(image_path):
    '''
    Convert any types of pic to png type. And save picture in cache folder.
    '''
    if not os.path.isfile(image_path):
        raise InternalError('File not found', 'File {0} does\'t exist'.format(image_path))
    f, e = os.path.splitext(image_path)
    if e.lower() == '.png':
        return
    else:
        o = f + '.png'
        im = Image.open(image_path)
        im.save(o, 'PNG')


class SMSSender(object):
    '''
    SMS Sender Class
    '''
    def __init__(self):
        self.app_name = APP_NAME
        self.company_name = COMPANY_NAME

    def init_app(self, app):
        self.app = app
        self.api_key = app.config['API_KEY']

    def tpl_send(self, mobile, code, tpl_id=SMS_TPL_REG):
        '''
        Send captcha message default.
        '''
        def wrapper():
            url = 'http://yunpian.com/v1/sms/tpl_send.json' 
            value = {
                    '#code#': code, 
                    '#app#': self.app_name, 
                    '#company#': self.company_name
                    }
            data = {
                    'apikey': self.api_key, 
                    'mobile': mobile, 
                    'tpl_id': tpl_id, 
                    'tpl_value': urllib.urlencode(value)
                    }
            response  = urllib2.urlopen(url, data=urllib.urlencode(data))
            d = json.loads(response.read())
            self.sms_id = d['result']['sid']
            if d['msg'] == 'OK':
                return True
            else:
                raise InternalError('Send SMS Error', d['msg'])
        thread.start_new_thread(wrapper, ())

def require_login(func):
    from flask import g, request
    from functools import wraps
    @wraps(func)
    def wrapper():
        from models import User
        from errors import ThrownError
        args = request.form
        filter(args, ('uid', 'auth', 'dd'))
        istimeout(args['dd'])
        u = User.query.filter(User.uid == int(args['uid'])).first()
        if u is None:
            raise ThrownError('User do not exists.')
        print hash(':'.join(u.token, args['dd'])), args['auth']
        if hash(':'.join([u.token, args['dd']])) != args['auth']:
            raise ThrownError('Wrong token.')
        g.user = u 
        g.args = args
        return func()
    return wrapper

if __name__ == '__main__':
    # convert2png('/var/www/letusgo/letusgo/avatar/cache/default.jpg')
    # print thumbnails('default')
    # tpl_send('13260614509', '123456', 6)
    pass
else:
    # if imported
    sms = SMSSender()
