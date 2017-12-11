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

    if imgURItoFile(image_URI, "signup"):
        register_new(username)
        return True
    return False


#returns username
def login(image_URI):

    if not imgURItoFile(image_URI, "login"):
        return None
    result = classify()   #todo, make sure unknown is saved and recent. This may cause problems if multiple people try and log in at once. Make separate, dedicated thread on server per login request?
    os.remove("unknown")  #cleanup

    return result

def imgURItoFile(data, state):
	if state == "login":
		fileName = "unknown"
	else:
		fileName = "signupPic.png"
	fh = open(fileName, "wb")
        try:
	    fh.write(str(data.split(",")[1].decode('base64')))
        except:
            return False
	fh.close()
        return True

