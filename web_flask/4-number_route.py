#!/usr/bin/python3
"""script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Outputs hello hbnb
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Outputs HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Outputs “C ” followed by value of text
    """
    new_text = text.replace('_', ' ')
    return "C " + new_text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Outputs  “Python ” followed by value of text
    """
    new_text = text.replace('_', ' ')
    return "Python " + new_text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Outputs "n is a number” only if n is an integer
    """
    return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
