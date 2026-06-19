import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    """Return a simple welcome message."""
    return jsonify(message="Welcome to the Sonar demo API")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify(status="ok")


@app.route("/user")
def get_user():
    """Look up a user by id from the database."""
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Planted issue: user input concatenated into SQL -> SQL injection
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return jsonify(users=rows)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
