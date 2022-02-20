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
Next create another two `.env` file, and put your google secret token in those files, keep one in the app directory, and another one in upload directory.

Run `docker-compose up --build -d`
The home page should be available on localhost 


