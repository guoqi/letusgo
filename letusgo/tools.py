#!/usr/bin/python
#coding: utf-8
from PIL import Image
import md5
import os

from globals import AVATAR_DIR, AVATAR_BIG_SIZE, AVATAR_SMALL_SIZE, DEFAULT_AVATAR_CACHE_DIR
from errors import InternalError

def hash(string):
    return md5.md5(string).hexdigest()

def genpath(*args):
    return os.sep.join(args)

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

if __name__ == '__main__':
    convert2png('/var/www/letusgo/letusgo/avatar/cache/default.jpg')
    print thumbnails('default')
