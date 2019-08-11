# Read Me for the Verv Flask Microservice

## Useful Links

For the Flask project look at [Flask](http://flask.pocoo.org)

The OpenAPI (swagger) library for Flask called [Connexion](http://connexion.readthedocs.io/en/latest)

The Flask dependancy injector, to make testing easier by removing the need for global Flask objects called [Flask Injector](http://pypi.org/project/Flask-Injector)

The non SQL DB which uses string value pairs and JSON to define attributes called [Couch DB](http://couchdb.apache.org/)

## Setup Tasks

1. ~~Setup a virtual environment for python 3.x~~ **Done**
2. ~~Setup a github repo for this project~~ **Done**
2. ~~Use pip to install Flask.~~ **Done**
3. ~~Use pip to install Connexion~~ **Done**
4. Use pip to install Flask-Injector
5. Setup and install CouchDB

## TODO Section
The todo section is for me to make a list of things to solve during this setup process
1) ~~Python 3.6 is not installed onto the local machine. Find out how to install it manually or use docker containers.~~ **Done**
2) ~~The 'F' notation is not supported on python.3.5 (e.g. f'Hello,..... ).~~ Use a work around for now. Using "string {}".format(x) for now. **Done**
3) ~~Setup a .gitignore to remove all the IDE and pycache files from git.~~ **Done**
4) ~~Create a requirements.txt file to hold all the installed python packages used on your system.~~ **Done**


### Setup Python 3.6 On local machine.
~~The local machine does not have 3.6 installed. Consider installing alongside 3.5 or using
a docker container.~~ **Done**

Use precompiled and setup PPA of python 3.6 to install onto a Ubuntu 14.x based machine. Then used virtualenv to setup python 3.6. Commands I used were:

```bash

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```


## Tasks
This section is a real time diary of what you did in setting up the system


### Task 1 Setup Virtual Environment
~~Create virtual environment, project directory and readme file~~ **Done**


Using commands:

``` bash
	/> mkvirtualenv --python=/usr/bin/python3.6 verv
	/> mkdir project
	/> mkdir documents
	/> touch documents/README.md
```

### Task 2 Setup github repo for this project
~~Setup a github repo for the project~~ **Done**

~~Create readme file~~ **Done**
```bash
https://github.com/nherriot/verv-flask/edit/master/documents/README.md
```
~~Create a .gitignore file to stop IDE and python cache, compile and xml files being stored on github.~~ **Done**
Using a .gitignore as:

```
# ignore .idea directory for pycharm IDE
**/.idea

# ignore __pycache__ files created by Flask
**/__pycache__

```


### Task 3 Setup Flask
1. ~~Get flask installed onto the system.~~ **Done**


Using the command:
```bash
   $ pip install -U Flask
```

2. ~~Ensure the development server can be run with a hello world app.~~ **Done**

Using the file /server/hello.py
Start the dev server with:
```bash

   $ python hello.py
   * Serving Flask app "hello" (lazy loading)
   * Environment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
   * Debug mode: off
   * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```

3. Create a scratch area for testing 'hello world' parts of the system.
4. ~~Create a requirements.txt to keep track of packages installed.~~ **Done**

Using the command:
```bash
   $ pip freeze > requirements.txt
```

### Task 4 Setup Connexion For Flask
~~Install the Connexion plugin~~ **Done**

Using the command:
```bash
   pip install connexion[swagger-ui]
```

Look up the Connexion plugin.
Find out how it works.
Make a hello world to prove it works, and place in the scratch area

### Task 5 Setup Flask-Injector
Look up the plugin.
Find out how it works.
Make a hello world test case in the scratch area.

### Task 6 Create A Getproduct Endpoint
Make a simple Flask server that allows a GET request on an endpoint called /getproduct
Hard code the endpoint as a json file with attributes like:
```json
   properties
      _id: {type:string}
      prodname: {type:string}
      catagory: {type:string}
      quantity: {type:number}
```

### Task 7 Create A Connexsions Endpoint Using Swagger
Make the same endpoint as above, but use the connexions Flask plugin

