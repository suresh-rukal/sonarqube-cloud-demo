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


@app.route("/user", methods=["GET"])
def get_user():
    """Look up a user by id from the database."""
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Planted issue 1 (security): user input concatenated into SQL -> SQL injection
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(users=rows)


@app.route("/status/<int:code>", methods=["GET"])
def status_label(code):
    """Return a human-readable label for a status code."""
    # Planted issue 2 (reliability): duplicate branch condition -> second is unreachable
    if code == 200:
        return jsonify(label="ok")
    elif code == 409:
        return jsonify(label="duplicate")
    return jsonify(label="other")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)


