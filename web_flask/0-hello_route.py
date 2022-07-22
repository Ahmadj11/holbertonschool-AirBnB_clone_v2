#!/usr/bin/python3
"""script starts Flask web application and defines route '/'"""

from flask import Flask
# create Flask application instance, passing it the name of the current module
app = Flask(__name__)


# decorator turns a python function into a Flask view function
@app.route('/', strict_slashes=False)
def hello():
    """function responds to web requests to the main URL"""
    return 'Hello HBNB!'

# start the flask application listening on host address and ports specificied
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
