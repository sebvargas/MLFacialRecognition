# InstallationDocs

## Docker-based software
If you are running your own Flask server, you can just use our backend.py file in redPanda in docker-files.  
- To run using our docker container, you must have Docker installed. Check the website below to install docker
https://www.docker.com/kubernetes#/CE

- Download our Docker folder named `docker-files` and stand the container up by


1) Starting Docker
2) Navigate to our Docker folder in terminal/console
3) navigate to the redPanda folder
4) execute `docker build -t cont1 .`
5) execute `docker run --name cont1 cont1`
6) Refer to API Docs on how to interact with the container

### for React.js
7) Use the urihelper.js file
8) Refer to API Docs on how to call its functions 

## Troubleshooting:

Taken from https://docs.docker.com/install/linux/linux-postinstall/  
Docker requires root access:  
Add the docker group if it doesn't already exist:  
`sudo groupadd docker`  
Add the connected user "$USER" to the docker group. Change the user name to match your preferred user if you do not want to use your current user:  
`sudo gpasswd -a $USER docker`  
Either do a `newgrp docker` or log out/in to activate the changes to groups.  
You can use  
`docker run hello-world`  
to check if you can run docker without sudo. 

