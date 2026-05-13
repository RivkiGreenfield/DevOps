"""Simple Flask application."""

import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint."""
    unused_variable = "fail pylint"




    return f"""
    <h1>👋 Hello from GitHub Actions + Docker! GUR SEMINARY</h1>
    <p>Version: {os.getenv('VERSION', '1.0.0')}</p>
    <p>Built at: {os.getenv('BUILD_TIME', 'unknown')}</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
