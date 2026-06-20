import sqlite3

from flask import Blueprint, jsonify, request

bp = Blueprint("lookup", __name__)

conn = sqlite3.connect("users.db", check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.executemany("INSERT OR IGNORE INTO users VALUES (?, ?)", [(1, "Alice"), (2, "Bob")])
conn.commit()


@bp.route("/lookup")
def lookup():
    user_id = request.args.get("id")
    row = conn.execute(f"SELECT id, name FROM users WHERE id = {user_id}").fetchone()
    if row:
        return jsonify(id=row[0], name=row[1])
    return jsonify(error="not found"), 404
