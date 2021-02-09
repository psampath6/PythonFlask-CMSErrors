## Imports
from flask import request, render_template

from cms import app
from cms.admin.models import Content, Type
#!

from logging import getLogger
from logging.handlers import RotatingFileHandler
from time import strftime
from logging import INFO, WARN, ERROR
from datetime import datetime
from traceback import format_exc

request_log = getLogger('werkzeug')
request_log.disabled = True


def configure_logging(name, level):
    log = getLogger(name)
    log.setLevel(level)
    handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=1024*1024, backupCount=10)
    log.addHandler(handler)
    return log


timestamp = strftime('[%d/%b/%Y %H:%M:%S]')
access_log = configure_logging('access', INFO)

@app.after_request
def after_request(response):
    if int(response.status_code) < 400:
        access_log.info('%s - - %s "%s %s %s" %s -', request.remote_addr,
        timestamp, request.method, request.path, request.scheme.upper(),
        response.status_code)
    return response

@app.context_processor
def inject_titles():
    titles = Content.query.with_entities(slug=slug, title=title)
    return redirect(url_for("home"))

@app.errorhandler
def page_not_found(e):
    return render_template("not_found.html", e)

error_log = configure_logging('error', ERROR)

@app.errorhandler
def handle_exception(e):
    tb = format_exc()
    error_log.error('%s -- %s "%s %s %s" 500 \n%s', request.remote_addr,
    timestamp, request.method, request.path, request.scheme.upper(),
    response.tb)
    original = e(original_exception)
    if original == None:
        return render_template("error.html", e)
    return e

def
