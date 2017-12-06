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

def register(POST_USERNAME, POST_PASSWORD, POST_IMAGE, POST_URL):

    imgURItoFile(POST_IMAGE, "signup")
    password_hashed = bcrypt.hashpw(POST_PASSWORD, bcrypt.gensalt())
    register_new(POST_URL,POST_USERNAME,password_hashed)
    imgURItoFile(POST_IMAGE, "signup")

    """
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
    """
    result = classify(POST_URL)

	if result:
		print("Registration Successful!")
	else:
		flash('Failed Registration')
        


def login(POST_IMAGE):
 
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
    

    result = classify()   #todo, make sure unknown is saved and recent. This may cause problems if multiple people try and log in at once. Make separate, dedicated thread on server per login request?
    os.remove("unknown")  #cleanup

    return log_in(POST_USERNAME, POST_PASSWORD)


def imgURItoFile(data, state):
	if state == "login":
		fileName = "loginPic.png"
	else:
		fileName = "signupPic.png"
	fh = open(fileName, "wb")
	fh.write(str(data.split(",")[1].decode('base64')))
	fh.close()

