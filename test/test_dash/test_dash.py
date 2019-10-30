from flask import Flask

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
        MyApp.construct_with_flask(server=app, url="/admin")

    def test_logger(self):
        x = MyApp(name="wurst")
        assert x.logger

class TestTuple(object):
    def test_tuple(self):
        server = Flask(__name__)
        tuple = AppTuple(dash=MyApp, href="/admin", text="MY TEXT")
        app = tuple.dash.construct_with_flask(server=server, url=tuple.href)
        assert isinstance(app, Dash)