import logging

from dash import html
from flask import Flask

from pyweb.pydash.common import App


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_layout(self):
        return html.H1("Hello World")

    def register_callback(self):
        return 2


def test_cache():
    x = MyApp(name="maffay")
    assert x.register_callback() == 2

def test_logger():
    x = MyApp(name="wurst")

    # there exists an logger
    assert x.logger

    # set the level for the logger
    x.logger.setLevel(logging.DEBUG)

    # no log messages
    assert x.logs == []

    x.logs = ["peter"]
    assert x.logs == ["peter"]

    x.logs = []
    assert x.logs == []

    x.logger.debug("tests")
    assert x.logs[0][-4:] == "tests"


def test_flask():
    app = Flask(__name__)
    app.config["Wurst"] = "Peter Maffay"

    dash = MyApp.dash_application(url="/admin")
    dash.init_app(app=app)

