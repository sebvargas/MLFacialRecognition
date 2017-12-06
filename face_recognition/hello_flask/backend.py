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

def register(POST_USERNAME, POST_PASSWORD, POST_IMAGE):
    imgURItoFile(POST_IMAGE, "signup")
    password_hashed = bcrypt.hashpw(POST_PASSWORD, bcrypt.gensalt())
    register_new(POST_URL,POST_USERNAME,password_hashed)

    if result:
    	print("Registration Successful!")
    else:
    	flash('Failed Registration')
    return register_confirm(POST_USERNAME, POST_PASSWORD, POST_IMAGE)


def login(POST_IMAGE):
 
    imgURItoFile(POST_IMAGE, "login")


    result = classify(POST_URL)
    os.remove("loginPic.png")  #cleanup

    return log_in(POST_USERNAME, POST_PASSWORD)

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
