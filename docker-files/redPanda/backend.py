from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import numpy as np
from PIL import Image
import re
import cStringIO
import io, base64
import sys
import shutil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

KNOWN_IMAGE_DIR = "known_images/"  #todo, make this absolute path

def register(username, image_URIs):
    os.makedirs(KNOWN_IMAGE_DIR + username + "/")   #todo try catch, multiple users same name?
    for i in range(0,len(image_URIs)):
	fileName = str(i)
        if imgURItoFile(str(i), image_URIs[i]):
            shutil.move(fileName,KNOWN_IMAGE_DIR + username)  #todo, check if image is already there
        else:
            print "ERROR in register!"
            return False
    return True


#returns username
def login(image_URIs,confidence):
    #todo, only checking 3
    for i in range(len(image_URIs)):
        if i == 0 and not imgURItoFile("unknown", image_URIs[i]):
            print 'i=1 failed'
            return None
        if i == 1 and not imgURItoFile("unknown_left", image_URIs[i]):
            print 'i=2 failed'
            return None
        if i == 2 and not imgURItoFile("unknown_right", image_URIs[i]):
            print 'i=3 failed'
            return None

        
    result = main.classify(KNOWN_IMAGE_DIR,confidence)   #todo, make sure unknown is saved and recent. This may cause problems if multiple people try and log in at once. Make separate, dedicated thread on server per login request?
    os.remove("unknown")  #cleanup
    os.remove("unknown_left")
    os.remove("unknown_right")

    return result

def imgURItoFile(fileName, data):

    fh = open(fileName, "wb")
    try:
	fh.write(str(data.split(",")[1].decode('base64')))
    except:
        return False
    fh.close()
    return True

