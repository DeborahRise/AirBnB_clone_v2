#!/usr/bin/python3
"""script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page:
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ To teardown storage after use """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
