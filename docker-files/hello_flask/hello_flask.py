from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import numpy as np
from PIL import Image
import re
import cStringIO
import io, base64
import sys
import backend


#todo, import these from backend
LOW_SECURITY = .6
MEDIUM_SECURITY = .5
HIGH_SECURITY = .4

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

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

@APP.route('/index')
def reroute():
    return render_template('index.html')
@APP.route('/newHtml')
def newHtml():
    return render_template('newhtml.html')

@APP.route('/home')
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

@APP.route('/register_failed')
def register_failed():
	session['logged_in'] = False

	return "Registration Failed!  <a href='/index'>Home</a>"

@APP.route('/register',  methods=['POST'])
def register():
    POST_USERNAME = str(request.form['username'])
    POST_IMAGE = str(request.form['imageUrl'])
    IMAGES = POST_IMAGE.split("#*^/")
    print "In register. Images len: " + str(len(IMAGES))
    print len(IMAGES)
    if backend.register(POST_USERNAME, IMAGES):
        return register_confirm(POST_USERNAME, POST_IMAGE)
    else:
        return register_failed()

@APP.route('/login', methods=['POST'])
def do_admin_login():
    POST_IMAGE = str(request.form['imageUrl'])
    POST_URL = str(request.form['txtUrl'])
    POST_URL = POST_URL.split('/')[-1]
    
    IMAGES = POST_IMAGE.split("#*^/")
    print "In register. Images len: " + str(len(IMAGES))
    
    result = backend.login(IMAGES,MEDIUM_SECURITY)
    if result != None:
        print "CLASSIFIED SUCCESSFULLY", result
        session['logged_in'] = True
    else:
        print "CLASSIFICATION FAILED"
        return log_in(None)
    return log_in(result)

@APP.route('/oldHtml')
def oldHtml():
    return render_template('oldhtml.html')

@APP.route('/back', methods=['POST'])
def back():
    return render_template('index.html')


if __name__ == '__main__':
	APP.secret_key = os.urandom(12)
	APP.debug=True
	APP.run(host="0.0.0.0")
