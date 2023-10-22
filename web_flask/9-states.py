#!/usr/bin/python3
"""Start web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    """Displays a html page with states
    """
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states, id=id)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
