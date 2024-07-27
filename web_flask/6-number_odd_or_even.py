#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template, abort


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """This function displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    This function displays 'display “C ”
    followed by the value of the text variable'
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
def python(text):
    """
    This function displays 'display “Python ”
    followed by the value of the text variable'
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This function displays 'n is a number'"""
    if type(n) == int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """This function displays 'n is a number'"""
    if type(n) == int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """This function displays 'n is a number'"""
    if type(n) == int:
        if n % 2 == 0:
            return render_template(
                    '6-number_odd_or_even.html',
                    number=n,
                    even_or_odd="even"
                    )
        else:
            return render_template(
                    '6-number_odd_or_even.html',
                    number=n,
                    even_or_odd="odd"
                    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
