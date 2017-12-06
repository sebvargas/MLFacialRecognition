from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import numpy as np
from PIL import Image
import re
import cStringIO
import io, base64
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import register_new, classify
import bcrypt

#database file name
engine = create_engine('sqlite:///tutorial.db', echo=True)


@APP.route('/hook', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
    image_PIL = Image.open(cStringIO.StringIO(image_b64))
    image_np = np.array(image_PIL)
    print 'Image received: {}'.format(image_np.shape)
    return ''

def register(POST_USERNAME, POST_PASSWORD, POST_IMAGE):

	imgURItoFile(POST_IMAGE, "signup")

    password_hashed = bcrypt.hashpw(POST_PASSWORD, bcrypt.gensalt())
    register_new(POST_URL,POST_USERNAME,password_hashed)

	Session = sessionmaker(bind=engine)
	session = Session()
	user = User(POST_USERNAME,password_hashed)
	session.add(user)
	# commit the record the database
	session.commit() 
	session.commit()
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
	result = query.first()

	if result:
		print("Registration Successful!")
	else:
		flash('Failed Registration')
        
	return register_confirm(POST_USERNAME, POST_PASSWORD, POST_IMAGE)


def do_admin_login(POST_IMAGE):
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_IMAGE = str(request.form['imageUrl'])
    POST_URL = str(request.form['txtUrl'])
    POST_URL = POST_URL.split('/')[-1]
    imgURItoFile(POST_IMAGE, "login")

    password_hashed = bcrypt.hashpw(POST_PASSWORD, bcrypt.gensalt())
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([password_hashed]))
    result = query.first()
    

    result = classify(POST_URL)
    os.remove("loginPic.png")  #cleanup

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
