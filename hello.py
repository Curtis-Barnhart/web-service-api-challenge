# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/api/myservice", methods=['GET'])
def hello_world():
    return "Hello, World!"
