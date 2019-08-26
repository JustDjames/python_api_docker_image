# Python Api Docker Image

This is the [basic python Api](https://github.com/JustDjames/basic_python_api) and it's webpage placed into docker images.

## Installation

### Requirements
* Docker ( install instructions [here](https://docs.docker.com/install/) )

### Setup

Once you have cloned this repo, navigate into the api directory and run the following command to build the image:

         docker build -t python_api:latest .
Or you can use the following command to pull the image from the docker repository
        
        docker pull callmedjay/python_api:latest
To build the webapage container navigate into the webpage directory and run the following command:

        docker build -t python_webpage:latest .

Or you can use the following command to pull from the docker repository

        docker pull callmedjay/python_webpage:latest 
### Usage

1) Once the api image is built ( or pulled ), run the container by using this command:

        docker run -p 5000:5000 python_api:latest

2) you can use a rest client like [insomnia](https://insomnia.rest/) or [postman](https://www.getpostman.com/) ( or just use curl )

3) To run the webpage run the following command (for the webpage work correctly the api image MUST be running in a container):

        docker run -d -p 80:80 webpage:latest
