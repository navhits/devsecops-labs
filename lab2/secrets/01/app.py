import flask

app = flask.Flask(__name__)


user_table = {
    "1": {
        "name": "Alice",
        "email": "alice@example.com"
    },
    "2": {
        "name": "Bob",
        "email": "bob@example.com"
    },
    "3": {
        "name": "Charlie",
        "email": "charlie@example.com"
    }
}


@app.route("/root")
def root():
    return {"message": "Hello World"}


@app.route("/auth/user/<user_id>")
def auth_user(user_id):
    if user_id not in user_table:
        return {"error": "User not found"}, 404
    user = user_table[user_id]
    return {"user": user}
