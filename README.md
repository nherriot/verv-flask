# Read Me for the Verv Flask Microservice

A repo that builds a simple REST API to fetch product information. It responds to HTTP GET requests to provide:

```json

properties
      _id: {type:string}
      prodname: {type:string}
      catagory: {type:string}
      quantity: {type:number}
      
```
This uses Flask, Connexion, Flask-Injector and Couch DB to achieve this.

## Prerequisits
Your computer will need to have Python 3.6 installed and setup on your system.
It is recommended that you use a [virtulenv](https://virtualenv.pypa.io/en/latest/) setup to follow this guide.

## To Install And Setup The Microservice
To setup your system you need to clone the repo and install all relevant packages.
To install the repo do:

```bash
  $ git clone https://github.com/nherriot/verv-flask.git
```

```bash
  $ pip install -r requirements.txt
```

## To Run The Server
To run the development server do:
```bash
  $ python verv.py 
  * Serving Flask app "verv" (lazy loading)
  * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
  * Debug mode: on
  * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 255-615-148
```

## To Test The Server
You can run curl scripts to test a good and bad example of fetching product information.
A postive response:
```bash
curl -X GET --header 'Accept: application/json' 'http://localhost:8000/v1.0/getproduct?prod_id=123'
{
  "_id": "123",
  "category": "Electric Meter",
  "prodname": "verv smartmeter v1",
  "quantity": 101
}
```

A negative response:
```bash
curl -X GET --header 'Accept: application/json' 'http://localhost:8000/v1.0/getproduct?prod_id=1234'
"No product with product ID: 1234"
```

## Swagger UI
To examin the API with swagger you can go to your browser and use the following URL:
  * http://localhost:8000/v1.0/ui/ *






verv flask microservice. Using 'flask', 'Couch DB', 'Connexion' and 'Flask-Injector'.
