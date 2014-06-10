#!/usr/bin/python
#coding: utf-8
from flask import Blueprint, Response, request
import os

from ..globals import AVATAR_DIR, PNG_MIMETYPE
from ..errors import ThrownError
from ..tools import filter

bp = Blueprint('img', __name__)

@bp.route('/avatar/<dir>/<filename>', methods=['GET'])
def avatar(dir, filename):
    path = os.sep.join([AVATAR_DIR, dir, filename])
    if not os.path.isfile(path):
        raise ThrownError('No such filename')
    f = open(path, 'r')
    bytes = f.read()
    f.close()
    return Response(bytes, mimetype=PNG_MIMETYPE)
