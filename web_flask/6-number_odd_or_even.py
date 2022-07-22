#!/usr/bin/python3
"""script starts Flask web application and defines route '/'"""

from flask import Flask, render_template
# create Flask application instance, passing it the name of the current module
app = Flask(__name__)


# decorator turns a python function into a Flask view function
@app.route('/', strict_slashes=False)
def hello():
    """funct responds to requests to the main URL diplaying 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """defining behavior for /hbnb url, display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """defining /c url behavior w dynamic capacity to display text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """define /python/<text> URL behavior"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """define behavior of /number/<n> URL where n must be integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """/number_template/<n> will return an HTML page if n is an int"""
    # render template will look in templates folder for html file designated
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """displays HTML page if N is int and which states if n is odd or even"""
    if (n % 2) == 0:  # the number is even
        ntype = 'even'
    else:  # the number is odd
        ntype = 'odd'
    # tell html template what variables from route def apply to html variables
    return render_template('6-number_odd_or_even.html', n=n, ntype=ntype)


# start the flask application listening on host address and ports specificied
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
