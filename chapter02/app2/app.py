from flask import Flask

app = Flask(__name__)


@app.route("/api2/go")
def api02():
    return "<p>Hello, API2!</p>"
