from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def index():
    return "<h1>Hello Azure! updated</h1>"
