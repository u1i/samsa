FROM u1ih/nodejs-ubuntu:1
MAINTAINER uli.hitzel@gmail.com
EXPOSE 8080
RUN mkdir /app
RUN apt-get update
RUN npm install -g api-spec-converter
RUN apt-get install -y python-pip
RUN pip install cherrypy bottle
COPY server.py /app/server.py
COPY samsa.py /app/samsa.py

CMD ["python","/app/server.py"]
