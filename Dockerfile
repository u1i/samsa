FROM u1ih/nodejs-ubuntu:1
MAINTAINER uli.hitzel@gmail.com
EXPOSE 8080
RUN mkdir /app
RUN apt-get update
RUN npm install -g api-spec-converter
RUN api-spec-converter --help
#COPY app /app

#CMD ["sh","/app/start.sh"]

