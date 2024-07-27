#!/usr/bin/python3
'''
This module starts a Flask web application
listening on 0.0.0.0, port 5000
with strict_slashes=True
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    ''' The homepage'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
