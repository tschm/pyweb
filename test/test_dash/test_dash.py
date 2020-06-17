import pytest
from flask import Flask

from pyutil.web.application import create_server
from pyweb.pydash.common import *
import dash_html_components as html


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


class TestDash(object):
    def test_cache(self):
        x = MyApp(name="maffay")
        assert x.register_callback() == 2

    def test_flask(self):
        app = Flask(__name__)
        app.config["Wurst"] = "Peter Maffay"
        x = MyApp.construct_with_flask(server=app, url="/admin")
        assert x.server.config["Wurst"] == "Peter Maffay"

    def test_logger(self):
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

    def test_not_implemented(self):
        with pytest.raises(NotImplementedError):
            MyApp2(name="wurst")

    def test_not_implemented_layout(self):
        with pytest.raises(NotImplementedError):
            x = MyApp3(name="wurst")
            x.build_layout()


def test_tuple():
    server = Flask(__name__)
    tuple = AppTuple(dash=MyApp, href="/admin", text="MY TEXT")
    app = tuple.dash.construct_with_flask(server=server, url=tuple.href)
    assert isinstance(app, Dash)


def test_create_server():
    server = create_server(template_folder=None, static_folder=None, extensions=[])
    app = MyApp.construct_with_flask(server, url="/test")
    assert app.server.config == server.config
