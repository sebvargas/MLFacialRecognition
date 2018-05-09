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
the more photos we take, the harder it becomes to fool our software. As of right now, we only have it capable of taking  
3 photos for logging in.  

You can also implement your own camera if you wish, as long as you pass the right arguments onto our backend

```javascript
<script>  
            var count = 0;  
            var num_of_images = 3;  
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

## React Component
Below is a React component that you could use, but feel free to use your own. The important part is to get the URIs of the images.

```javascript
import Webcam from 'react-webcam';
class SignUp extends Component {
  setRef = (webcam) => {
    this.webcam = webcam;
  }
 
  capture = () => {
    const imageSrc = this.webcam.getScreenshot();
    alert(imageSrc);
  };

    render() {

        return (
                <img
              style={style.captureImage}
              ref={(img) => {
                this.img = img;
              }}
                />

            <Webcam
              audio={false}
              height={150}
              ref={this.setRef}
              screenshotFormat="image/jpeg"
              width={150}
            />
            )
        };
```

and call
```javascript                                 
var imgSrc = this.webcam.getScreenshot();
```

on the button you want to take the picture of.

If you would like to take multiple pictures, you can do something like this: 
```javascript
            alert("Look straight into the camera");
            var imgSrc0 = this.webcam.getScreenshot();
            alert("Turn your whole head right");
            var imgSrc1 = imgSrc + "#*^/" + this.webcam.getScreenshot();
            alert("Turn your whole head left");
            var imgSrc = imgSrc2 + "#*^/" + this.webcam.getScreenshot();
```

imgSrc would be the URI values that you would pass onto the backend.

Note: This set of characters "#*^/" is used to identify each individual URI if there is more than one being sent  


# Backend

## if using a Flask backend

You may want to just import our backend.py

Our backend simply uses 2 main functions

registers a username and links the images taken to that username  
This function would be called when the user registers for a new account  
@params username is a string that the user inputs when registering  
@image_URIs are the images that have been taken of the user given as an array of images  
`def register(username, image_URIs):  `


returns username  
 logs a user into an account that has been tied to their face or  
 fails a log in if a user has not been registered yet.  
 @params image_URI are the 3 images that have been taken of the user given as an array of images  
 where it is the picture of the front of their face, their left face profile and right face profile in that order
`def login(image_URIs,confidence): ` 

## React Backend

We have a uriHelper.js file that can be imported into a Node.js backend.  
The file can be found in the docker-files folder
Simply import the module and the following functions can be called where they are necessary  
  

Takes the username and the picture of the user when they register and returns an  
error if the user was not successfully registered  
@username must be a string  
@uri must be the URI of the image that is encoded in base64  
`registerHelper(username, uri)`

Takes the username and an array of URIs of pictures of the user and     
returns true if the user is verified and false otherwise  
@username must be a string  
@uris must be an array of 3 images of the user where it is the picture of the front of their face, their left face profile and right   face profile in that order, each encoded in base64  
`loginhelper(username,uris)`



Examples:
## Try It Out!
To try a proof of concept of our software, go to our hello_flask folder in docker-files do the following  
1) start docker
2) docker build -t hello_flask .
3) docker run --name hello_flask hello_flask
4) Go to 

## Sample Website
We integrated our software into a clone of usesparespace.com and using a similar mongodb backend, we've passed  
on the values we needed in some of their other fields since we had limited experience with React.  
To start up a clone you must have the following installed in addition to our installation docs:

1. [React](https://reactjs.org/)
2. [Express.js](https://expressjs.com/)
3. [Mongodb](https://www.mongodb.com/)
4. [Node.js](https://nodejs.org/en/)

Then once npm is installed, do npm install on each of the following:  
5. [travis-ci](https://travis-ci.org/)  
6. [mocha](https://mochajs.org/)  
7. [eslint](https://eslint.org/)  
8. [chai](http://chaijs.com/)  
9. [nodemailer](https://nodemailer.com/about/)  
10. [mongoose](http://mongoosejs.com/)  

then navigate to the sparespacefrontend folder and run
`npm install && npm start`  
do the same but inside the sparespacedevelop folder. After which, the sparespace clone website should open up  

then build and run our container  
1) Starting Docker
2) Navigate to our docker-files folder in terminal/console
3) navigate to the redPanda folder
4) execute `docker build -t cont1 .`
5) execute `docker run --name cont1 cont1`

and the site should have a functioning sign up and log in!  

