FROM python:2.7.14
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install python-dbus
RUN pip install PIL

COPY entrypoint.sh ./
COPY credential_manager.py ./

CMD [ "sh", "entrypoint.sh" ]
