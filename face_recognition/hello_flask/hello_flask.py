from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
#engine = create_engine('sqlite:///tutorial.db', echo=True)
import numpy as np
from PIL import Image
import re
import cStringIO
import io, base64
import sys
from main import register_new, classify
import backend

# Create the application.
APP = Flask(__name__)
APP.config

@APP.route('/hook', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
    image_PIL = Image.open(cStringIO.StringIO(image_b64))
    image_np = np.array(image_PIL)
    print 'Image received: {}'.format(image_np.shape)
    return ''

@APP.route('/index')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

@APP.route('/newHtml')
def newHtml():
    return render_template('newhtml.html')

@APP.route('/')
def home(POST_USERNAME):
    if not session.get('logged_in'):
    	return "log in failed. Click New User <a href='/index'>Back</a>"
    else:
    	session['logged_in'] = False
        return "Hello " +  POST_USERNAME  + "  <a href='/index'>Logout</a>" 

@APP.route('/log_in')
def log_in(POST_USERNAME):
    if POST_USERNAME == None:
    	return "log in failed. Click New User <a href='/index'>Back</a>"
    else:
    	session['logged_in'] = False
        return "Hello " +  POST_USERNAME  + "  <a href='/index'>Logout</a>" 

@APP.route('/register_confirm')
def register_confirm(POST_USERNAME, POST_IMAGE):
	session['logged_in'] = False

	return "You have registered! " +  POST_USERNAME  + "  <a href='/index'>Home</a>"

@APP.route('/register',  methods=['POST'])
def register():
    POST_USERNAME = str(request.form['username'])
    POST_IMAGE = str(request.form['imageUrl'])
    backend.register(POST_USERNAME, POST_IMAGE)
    return register_confirm(POST_USERNAME, POST_IMAGE)

@APP.route('/login', methods=['POST'])
def do_admin_login():
    POST_IMAGE = str(request.form['imageUrl'])
    POST_URL = str(request.form['txtUrl'])
    POST_URL = POST_URL.split('/')[-1]
    backend.imgURItoFile(POST_IMAGE, "login")
    result = backend.login(POST_IMAGE)
    if result != None:
        print "CLASSIFIED SUCCESSFULLY", result
        session['logged_in'] = True
    else:
        print "CLASSIFICATION FAILED"
    return log_in(result)

@APP.route('/oldHtml')
def oldHtml():
    return render_template('oldhtml.html')

@APP.route('/back', methods=['POST'])
def back():
    return render_template('index.html')

def imgURItoFile(data, state):
	if state == "login":
		fileName = "loginPic.png"
	else:
		fileName = "signupPic.png"
	fh = open(fileName, "wb")
	fh.write(str(data.split(",")[1].decode('base64')))
	fh.close()

if __name__ == '__main__':
	APP.secret_key = os.urandom(12)
	APP.debug=True
	APP.run()
