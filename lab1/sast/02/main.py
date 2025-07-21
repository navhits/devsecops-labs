import os

import flask

app = flask.Flask(__name__)


@app.route("/route_param")
def route_param():
    return os.system("ls -al")


@app.route("/route_param/<route_param>")
def route_param(route_param):
    return os.system("cat" + route_param)
