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

You can also implement your own camera if you wish, as long as you pass the right arguments onto our backend

```javascript
<script>  
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
                navigator.mediaDevices.getUserMedia(mediaConfig).then(function(  stream) {  
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
                       document.getElementById("canvas").appendChild(  convertCanvasToImage(canvas));  
            }, false);  
</script>  
```

Then for the body of the HTML, you must have these named fields
for the video, as well as 
```HTML
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
```
# Backend

## if using a Flask backend

You may want to just import our backend.py

Our backend simply uses 2 main functions

registers a username and links the images taken to that username
This function would be called when the user registers for a new account
@params username is a string that the user inputs when registering
@image_URIs are the images that have been taken of the user given as an array of images
def register(username, image_URIs):


returns username
 logs a user into an account that has been tied to their face or
 fails a log in if a user has not been registered yet.
 @params image_URI are the images that have been taken of the user given as an array of images
def login(image_URIs,confidence):

## React Backend

We have a uriHelper.js file that can be imported into a Node.js backend.  
The file can be found in the docker-files folder
Simply import the module and the following functions can be called where they are necessary  
  

// Takes the username and the picture of the user when they register and returns an  
// error if the user was not successfully registered  
// username must be a string  
// uri must be the URI of the image that is encoded in base64  
registerHelper(username, uri)

// Takes the username and an array of URIs of pictures of the user and     
// returns true if the user is verified and false otherwise  
// username must be a string  
// uris must be an array of images of the user, each encoded in base64  
loginhelper(username,uris)



There is an example of Flask Backend usage that will run with the front end provided as hello_flask.py


