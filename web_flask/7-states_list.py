#!/usr/bin/python3
"""script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page:
    """
    states = storage.all(State).order_by(State.name).all()

    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
