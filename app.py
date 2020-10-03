from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1>Hello Azure! hello</h1>"

@app.route("/")
def index():
    return "<h1>Hello Azure! index page</h1>"
