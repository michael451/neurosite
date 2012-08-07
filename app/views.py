"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""

from google.appengine.api import mail

from flask import Module, url_for, render_template, request, redirect

"""
from models import Todo
from forms import TodoForm, EmailForm
"""

views = Module(__name__, 'views')


@views.route('/')
def index():
    """Render website's index page."""
    return render_template('index.html')

@views.route('/faculty')
def faculty():
    return render_template('faculty.html')

@views.route('/curriculum')
def curriculum():
    return render_template('curriculum.html')

@views.route('/research')
def research():
    return render_template('research.html')

@views.route('/howtoapply')
def howtoapply():
    return render_template('howtoapply.html')

@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
