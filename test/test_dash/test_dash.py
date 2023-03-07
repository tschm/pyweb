import pytest
from dash import html
from flask import Flask

from pyweb.pydash.common import *


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_layout(self):
        return html.H1("Hello World")

    def register_callback(self):
        return 2


class MyApp2(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp3(App):
    def register_callback(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp4(App):
    def build_layout(self):
        return html.H1("Hello World")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


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

    x.logger.debug("test")
    assert x.logs[0][-4:] == "test"


def test_not_implemented():
    with pytest.raises(NotImplementedError):
        MyApp2(name="wurst")


def test_not_implemented_layout():
    with pytest.raises(NotImplementedError):
        x = MyApp3(name="wurst")
        x.build_layout()


def test_not_implemented_callback():
    with pytest.raises(NotImplementedError):
        x = MyApp4(name="wurst")
        x.register_callback()


def test_cache():
    x = MyApp(name="maffay")
    assert x.register_callback() == 2


def test_flask():
    app = Flask(__name__)
    app.config["Wurst"] = "Peter Maffay"

    dash = MyApp.dash_application(url="/admin")
    dash.init_app(app=app)


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

    x.logger.debug("test")
    assert x.logs[0][-4:] == "test"


def test_not_implemented():
    with pytest.raises(NotImplementedError):
        MyApp2(name="wurst")


def test_not_implemented_layout():
    with pytest.raises(NotImplementedError):
        x = MyApp3(name="wurst")
        x.build_layout()


def test_not_implemented_callback():
    with pytest.raises(NotImplementedError):
        x = MyApp4(name="wurst")
        x.register_callback()
