## Imports
from flask import request, render_template

from cms import app
from cms.admin.models import Content, Type
#!

from logging import getLogger
from logging.handlers import RotatingFileHandler
from time import strftime
from datetime import datetime

request_log = getLogger('werkzeug')
request_log.disabled = True


def configure_logging(name, level):
    log = getLogger(name)
    log.setLevel(level)
    handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=1024*1024, backupCount=10)
    log.addHandler(handler)
    return log


timestap = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
access_log = configure_logging('access', 'INFO')

def after_request():
    info()
