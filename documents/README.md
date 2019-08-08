# Read Me for the Verv Flask Microservice

## Useful Links

For the Flask project look at [Flask](http://flask.pocoo.org)

The OpenAPI (swagger) library for Flask called [Connexion](http://connexion.readthedocs.io/en/latest)

The Flask dependancy injector, to make testing easier by removing the need for global Flask objects called [Flask Injector](http://pypi.org/project/Flask-Injector)

The non SQL DB which uses string value pairs and JSON to define attributes called [Couch DB](http://couchdb.apache.org/)

## Setup Tasks

1. Setup a virtual environment for python 3.x
2. Setup a github repo for this project
2. Use pip to install Flask.
3. Use pip to install Flask-Injector
4. Setup and install CouchDB

## Work To Complete
1. Create an endpoint 'getproduct'

## TODO Section
The todo section is for me to make a list of things to solve during this setup process
1) Python 3.6 is not installed onto the local machine. Find out how to install it manually or use docker containers.
2) The 'F' notation is not supported on python.3.5 (e.g. f'Hello,..... ). Use a work around for now.

### Setup Python 3.6 On local machine.
The local machine does not have 3.6 installed. Consider installing alongside 3.5 or using
a docker container.

## Tasks
This section is a real time diary of what you did in setting up the system

### Task 1 Setup Virtual Environment
Create virtual environment, project directory and readme file with:

` bash
	/> mkvirtualenv --python=/usr/bin/python3.6 verv-flask3-6
	/> mkdir project
	/> mkdir documents
	/> touch documents/README.md
`

### Task 2 Setup github repo for this project
Setup a github repo for the project.
Create readme file.


### Task 3 Setup Flask
Get flask installed onto the system.
Ensure the development server can be run with a hello world app.

### Setup Connexion For Flask
Look up the Connexion plugin.
Find out how it works.



