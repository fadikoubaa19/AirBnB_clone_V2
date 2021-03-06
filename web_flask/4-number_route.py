#!/usr/bin/python3
''' task 2'''
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def main():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def route(text):
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Pyfun(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def integer(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
