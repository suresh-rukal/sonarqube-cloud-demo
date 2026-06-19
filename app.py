from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Return a simple welcome message."""
    return jsonify(message="Welcome to the Sonar demo API")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
