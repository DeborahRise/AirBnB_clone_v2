#!/usr/bin/python3
"""script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page:
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """
    display a HTML page:
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """ To teardown storage after use """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
