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

def register(POST_USERNAME, POST_IMAGE, POST_URL):

    imgURItoFile(POST_IMAGE, "signup")
    register_new(POST_USERNAME)
    imgURItoFile(POST_IMAGE, "signup")

#returns username
def login(POST_IMAGE):
 
    imgURItoFile(POST_IMAGE, "login")
    result = classify()   #todo, make sure unknown is saved and recent. This may cause problems if multiple people try and log in at once. Make separate, dedicated thread on server per login request?
    os.remove("unknown")  #cleanup

    return result

def imgURItoFile(data, state):
	if state == "login":
		fileName = "unknown"
	else:
		fileName = "signupPic.png"
	fh = open(fileName, "wb")
	fh.write(str(data.split(",")[1].decode('base64')))
	fh.close()

