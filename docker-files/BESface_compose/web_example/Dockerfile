FROM ubuntu:latest
MAINTAINER Sebastian Vargas “avargas@zagmail.gonzaga.edu”
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python
COPY . /app
COPY entrypoint.sh ./
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT python app.py
