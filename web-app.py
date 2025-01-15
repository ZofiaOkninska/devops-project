#!/usr/bin/env python 

from flask import Flask
import math

app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/hello/<name>')
def hello_name(name) :
	return 'Hello %s!' % name

@app.route('/goodbye/<name>')
def goodbye_name(name) :
	return 'Goodbye %s!' % name

@app.route('/')
# '/' URL is bound with hello_world() function.
def hello_world():
	return f'Hello, PI number equals: {math.PI}'

if __name__ == '__main__':
	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host='0.0.0.0', port=5001, debug=True)