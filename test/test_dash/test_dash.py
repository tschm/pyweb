import dash_html_components as html
import pytest
from flask import Flask

from pyweb.pydash.common import *
from pyweb.web.application import create_server


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


class TestDash:
    def test_cache(self):
        x = MyApp(name="maffay")
        assert x.register_callback() == 2

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

    def test_not_implemented_callback(self):
        with pytest.raises(NotImplementedError):
            x = MyApp4(name="wurst")
            x.register_callback()


class TestDash2:
    def test_cache(self):
        x = MyApp(name="maffay")
        assert x.register_callback() == 2

    def test_flask(self):
        app = Flask(__name__)
        app.config["Wurst"] = "Peter Maffay"

        dash = MyApp.dash_application(url="/admin")
        dash.init_app(app=app)

        # assert x.server.config["Wurst"] == "Peter Maffay"

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

    def test_not_implemented_callback(self):
        with pytest.raises(NotImplementedError):
            x = MyApp4(name="wurst")
            x.register_callback()
