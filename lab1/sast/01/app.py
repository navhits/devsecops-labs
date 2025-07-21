import flask

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):
    return eval(route_param)


@app.route("/route_param/<route_param>")
def route_param(route_param):
    return eval("hello")


@app.route("/get_param", methods=["GET"])
def get_param():
    param = flask.request.args.get("param")
    eval(param)

@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    eval("import " + flask.request.args.get("param"))


@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    param = flask.request.args.get("param")
    eval(param + "+ 'hello'")


@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    param = flask.request.args.get("param")
    eval("import {}".format(param))


@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    param = flask.request.args.get("param")
    eval("import %s" % (param,))


@app.route("/format", methods=["POST"])
def format():
    param = "{}".format(flask.request.form['param'])
    eval(param)


@app.route("/ok")
def ok():
    eval("This is fine")
