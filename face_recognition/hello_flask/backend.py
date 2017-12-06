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

def register(username, image_URI):

    imgURItoFile(image_URI, "signup")
    register_new(username)


#returns username
def login(image_URI):
 
    imgURItoFile(image_URI, "login")
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

