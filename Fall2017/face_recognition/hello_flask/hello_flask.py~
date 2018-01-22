from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
import numpy as np
from PIL import Image
import re
import cStringIO
import io, base64
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import register_new, classify

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
def home(POST_USERNAME, POST_PASSWORD):
    if not session.get('logged_in'):
    	return "log in failed. Click New User <a href='/index'>Back</a>"
    else:
    	session['logged_in'] = False
        return "Hello " +  POST_USERNAME + " " + POST_PASSWORD + "  <a href='/index'>Logout</a>" 

@APP.route('/log_in')
def log_in(POST_USERNAME, POST_PASSWORD):
    if not session.get('logged_in'):
    	return "log in failed. Click New User <a href='/index'>Back</a>"
    else:
    	session['logged_in'] = False
        return "Hello " +  POST_USERNAME + " " + POST_PASSWORD + "  <a href='/index'>Logout</a>" 

@APP.route('/register_confirm')
def register_confirm(POST_USERNAME, POST_PASSWORD, POST_IMAGE):
	print(str(POST_IMAGE))
	session['logged_in'] = False

	return "Hello " +  POST_USERNAME + " " + POST_PASSWORD + "  <a href='/index'>Logout</a>"

@APP.route('/register',  methods=['POST'])
def register():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])
	POST_IMAGE = str(request.form['imageUrl'])
	POST_URL = str(request.form['txtUrl'])
        POST_URL = POST_URL.split('/')[-1]
	imgURItoFile(POST_IMAGE, "signup")

        register_new(POST_URL,POST_USERNAME,POST_PASSWORD)

        '''
	Session = sessionmaker(bind=engine)
	session = Session()
	user = User(POST_USERNAME,POST_PASSWORD)
	session.add(user)
	# commit the record the database
	session.commit() 
	session.commit()
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
	result = query.first()
	#image_b64 = request.values['imageBase64']
	#image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
	#image_PIL = Image.open(cStringIO.StringIO(image_b64))
	#image_np = np.array(image_PIL)
	#print 'Image received: {}'.format(image_np.shape)
	if result:
		print("Registration Successful!")
	else:
		flash('Failed Registration')
        '''
	return register_confirm(POST_USERNAME, POST_PASSWORD, POST_IMAGE)


@APP.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_IMAGE = str(request.form['imageUrl'])
    POST_URL = str(request.form['txtUrl'])
    POST_URL = POST_URL.split('/')[-1]
    imgURItoFile(POST_IMAGE, "login")

    '''
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    '''

    result = classify(POST_URL)
    os.remove("loginPic.png")  #cleanup
    print result
    if result != False:
        print "CLASSIFIED SUCCESSFULLY", result[0], result[1]
        session['logged_in'] = True
    else:
        print "CLASSIFICATION FAILED"
        print('wrong password!')
    return log_in(POST_USERNAME, POST_PASSWORD)

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
