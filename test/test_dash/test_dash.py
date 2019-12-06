from flask import Flask

from pyweb.application import create_server
from pyweb.pydash.common import *
import dash_html_components as html


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_layout(self):
        return html.H1("Hello World")

    def register_callback(self):
        return 2


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
        assert x.logger
        x.logger.setLevel(logging.DEBUG)
        handler = DashLogger()
        handler.setLevel(logging.DEBUG)
        x.logger.addHandler(handler)
        x.logger.debug("test")
        assert x.logs == ["test"]
        x.logs = []
        assert x.logs == []


class TestTuple(object):
    def test_tuple(self):
        server = Flask(__name__)
        tuple = AppTuple(dash=MyApp, href="/admin", text="MY TEXT")
        app = tuple.dash.construct_with_flask(server=server, url=tuple.href)
        assert isinstance(app, Dash)
        

    def test_create_server(self):
        server = create_server(template_folder=None, static_folder=None, extensions=[])
        app = MyApp.construct_with_flask(server, url="/test")
        assert app.server.config == server.config

        