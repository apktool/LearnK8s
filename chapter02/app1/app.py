from flask import Flask

app = Flask(__name__)


@app.route("/api1/go")
def api01():
    return "<p>Hello, API1!</p>"
