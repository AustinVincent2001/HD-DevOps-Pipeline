"""
Simple Flask application for DevOps pipeline demonstration.
"""
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    def insecure_function():
      """
       Intentional insecure code for Bandit demonstration.
      """
    subprocess.Popen("dir", shell=True)
    """
    Home route.
    """
    return "Real Docker CI/CD Pipeline Running"
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000, debug=True)