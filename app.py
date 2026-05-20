"""
Simple Flask application for DevOps pipeline demonstration.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route.
    """
    return "DevOps Pipeline Working Successfully"

if __name__ == "__main__":
    app.run(debug=True)