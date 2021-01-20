#!/usr/bin/python3
''' task 2'''
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def intHtml(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def slash_number_odd_or_even(n):
    e_o = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, e_o=e_o)


if __name__ == "__main__":
    app.run()
