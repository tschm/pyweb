import pandas as pd
from flask import Flask, request

from pyweb.web.parser import respond_pandas

frame = pd.DataFrame(index=["A"], columns=["B"], data=[[3.0]])


app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/csv")
def csv():
    return respond_pandas(frame=frame, fmt="csv")


@app.route("/json")
def json():
    return respond_pandas(frame=frame, fmt="json")


@app.route("/post", methods=("POST",))
def post_hello():
    if request.method != "POST":
        raise AssertionError
    return "Hello Thomas!"
