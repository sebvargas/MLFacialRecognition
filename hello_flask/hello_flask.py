#!/usr/bin/env python

import flask
import os
from PIL import *
from flask import Flask, flash, redirect, render_template, request, session, abort

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/index')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@APP.route('/newHtml')
def newHtml():


    return flask.render_template('newHtml.html')

@APP.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        print("asdasdas")

    else:
        flash('wrong password!')

    print("bob")
    print(request.form['password'])
    print(request.form['username'])

    return newHtml()

@APP.route('/oldHtml')
def oldHtml():
    return flask.render_template('oldHtml.html')

@APP.route('/addContact')
def addContact():
    return flask.render_template('addContact.php')

if __name__ == '__main__':
	APP.secret_key = os.urandom(12)
	APP.debug=True
	APP.run()