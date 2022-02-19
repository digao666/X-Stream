Hi

We are X stream !!!

Welcome to use our video streaming service.

There are 6 microservice in our architecture

Main app web server
Upload app web server
File system server
Database server
Authentication Server
Nginx Proxy Server

How to use?
This streaming service requires docker
Please download and extract the source code
cd to the root directory of our app

Creat a `.env` file and put your google authentication information in the file.
Next put your google secret token in `.env` file, keep it in the app directory, then copy it to the upload direcoty as well.

Run `docker-compose up --build -d`
The home page should be available on localhost 


