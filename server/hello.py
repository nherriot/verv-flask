from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello, {}!'.format(name)


app.run(host='0.0.0.0', port=8000)

