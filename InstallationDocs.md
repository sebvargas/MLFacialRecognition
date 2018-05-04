#InstallationDocs

# Docker-based software
If you are running your own Flask server, or would rather not use Docker, skip this.
- To run using our docker container, you must have Docker installed. Check the website below to install docker
https://www.docker.com/kubernetes#/CE

- Download our Docker folder named `docker-files` and stand the container up by


Docker requires root access:
Add the docker group if it doesn't already exist:
`sudo groupadd docker`
Add the connected user "$USER" to the docker group. Change the user name to match your preferred user if you do not want to use your current user:
`sudo gpasswd -a $USER docker`
Either do a `newgrp docker` or log out/in to activate the changes to groups.
You can use
`docker run hello-world`
to check if you can run docker without sudo.



1) Starting Docker
2) Navigate to our Docker folder in terminal/console
3) navigate to BESface_compose
4) execute `docker-compose build`
5) execute `docker-compose up`
6) Now your docker container should be up and running on http://127.0.0.1:5000/.



# Straight-Flask
0) Install these dependencies

	- Python 2.7
	- Tensorflow
	- Flask
	- Image
	- django < 2
	- Numpy
	- Pillow
	- face_recognition
1) To install our software, download our *place holder name of folder of software* within the same directory as either your current Flask application folder, or at the same directory level as your current backend folder

2) Refer to API Documentation for usage of our functions
