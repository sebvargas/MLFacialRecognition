FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    pkg-config \
    python2.7 \
    python2.7-dev \
    python-numpy \
    python3-pip \
    python3 \
    python-dev \
    python-numpy \
    python-pip \
    software-properties-common \
    zip
#RUN apt-get install -y python3 python3-pip python3-dev build-essential
COPY /known_images /app/known_images
COPY . /app
#COPY entrypoint.sh ./
WORKDIR /app
RUN pip2 install -r requirements.txt
RUN pip2 install numpy --upgrade
ENTRYPOINT python2 hello_flask.py