# API Documentation for Flask Backend with JavaScript frontend  


This API is designed to allow web developers to implement a facial recognition
log-in feature onto their websites that can either coexist with current username
password combinations, or replace them entirely. This will have to seperate components,
the Front end and back end.


## HTML Front End

Our front end works with any JavaScript or HTML based front end. We use hidden fields as well as 
camera access through JavaScript. To implement the camera onto your website, add this segment into your
script tag on the page where you would want your log-in to occur.

We implement facial recognition that captures multiple images of the user's face to be able to use a
time series to detect

(1) Whether it is the valid user
(2) Whether the camera is not being tricked by a physical photo of the valid user

The variable `num_of_images` determines how many photos of the user we would take,
the more photos we take, the harder it becomes to fool our software

`<script>
            var count = 0;
            var num_of_images = 5;
            var images = "";

            window.addEventListener("DOMContentLoaded", function() {
            // Grab elements, create settings, etc.
            var canvas = document.getElementById('canvas');
            var context = canvas.getContext('2d');
            var video = document.getElementById('video');
            document.getElementById('txtUrl').value = window.location.href;

            var mediaConfig =  { video: true };
            var errBack = function(e) {
                console.log('An error has occurred!', e)
            };

            // Put video listeners into place
            if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia(mediaConfig).then(function(stream) {
                    video.src = window.URL.createObjectURL(stream);
                    video.play();
                });
            }

            // Trigger photo take
            document.getElementById('snap').addEventListener('click', function() {

                context.drawImage(video, 0, 0, 640, 480);
                var canvas = document.getElementById('canvas');
                var dataURL = canvas.toDataURL();
	        images = images + dataURL;
                document.getElementById('imageUrl').value = images;

   	    for (i=1; i < num_of_images; i++) {
			      images = images + "#*^/";
			      setTimeout(wait(i), 3000);
		}

            });

            function wait(i) {
                alert(i);
                context.drawImage(video, 0, 0, 640, 480);
                var canvas = document.getElementById('canvas');
 	        var dataURL = canvas.toDataURL();
			  images = images + dataURL;
                document.getElementById('imageUrl').value = images;
            }
                       document.getElementById("canvas").appendChild(convertCanvasToImage(canvas));

            }, false);
        
</script>
`
Then for the body of the HTML, you must have these named fields
for the video, as well as 

<center>
<video id="video" width="640" height="480" style="border: 1px solid black;" autoplay></video>
<canvas id="canvas" width="640" height="480"  style="border: 1px solid black;"></canvas>
<form method="post" action="/register" autocomplete="on">
    Username:<input type="text" name="username" id="username" required><br>
    <input type="hidden" id="txtUrl" name="txtUrl" value="" />
    <input type="hidden" id="imageUrl" name="imageUrl" value="" />
    <input id="snap" type="submit" id="snap" value="Log in">
</form>
<form method="post" action="/back">
    <input type="submit" value="back">
</form>
</center>

#Backend

Our backend simply uses 2 main functions

registers a username and links the images taken to that username
This function would be called when the user registers for a new account
@params username is a string that the user inputs when registering
@image_URIs are the images that have been taken of the user
def register(username, image_URIs):


returns username
 logs a user into an account that has been tied to their face or
 fails a log in if a user has not been registered yet.
 @params image_URI are the images that have been taken of the user
def login(image_URIs,confidence):



Example of Flask Backend usage that will run with the front end provided

`
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
    if not backend.imgURItoFile(POST_IMAGE, "login"):
        return log_in(None)
    result = backend.login(POST_IMAGE,MEDIUM_SECURITY)
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


if __name__ == '__main__':
	APP.secret_key = os.urandom(12)
	APP.debug=True
	APP.run()
`
