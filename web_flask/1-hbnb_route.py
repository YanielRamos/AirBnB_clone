#!/usr/bin/python3
from flask import Flask
"""Script that prints HBNB with /hbnb"""


app = Flask(__name__)

app.route('/', strict_slashes=False)
def hello():
    """prints Hello hbnb!"""
    return "Hello HBNB!"

app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """prints HBNB"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)