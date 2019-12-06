# Meta tags for viewport responsiveness
import logging
from abc import ABCMeta, abstractmethod
from collections import namedtuple

from dash import Dash
from flask.helpers import get_root_path

style = {'width': '96%', 'display': 'inline-block', 'padding': 10}

AppTuple = namedtuple('App', ['dash', 'href', 'text'])

# don't delete; every app can use this functionality
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Output, Input, State
import dash_table


class DashLogger(logging.Handler):
    def __init__(self, fmt=None):
        super().__init__()
        self.logs = list()
        self.setFormatter(logging.Formatter(fmt=fmt))

    def emit(self, record):
        #try:
        self.logs.insert(0, self.format(record))
        #except Exception:
        #    self.handleError(record)


class App(Dash):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # only store the name of the function here, do not call build_layout()!
        self.layout = self.build_layout
        # register the callbacks
        self.register_callback()
        # let's not have any loggers
        self.logger.handlers = []

    @property
    def logs(self):
        # try all logger handlers and fish for logs method? Very weird, but works...
        for handler in self.server.logger.handlers:
            try:
                return handler.logs
            except AttributeError:
                pass

        return []

    @logs.setter
    def logs(self, value):
        for handler in self.server.logger.handlers:
            try:
                handler.logs = value
            except AttributeError:
                print("A")
                pass

    @abstractmethod
    def build_layout(self):
        raise NotImplementedError()

    @abstractmethod
    def register_callback(self):
        raise NotImplementedError()

    def serve(self, port=8050, name=None):
        from waitress import serve
        print("http://localhost:{port}/{name}".format(port=port, name=name))
        serve(app=self.server, port=port)

    @classmethod
    def construct_with_flask(cls, server, url):
        meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

        x = cls(name=__name__,
                server=server,
                url_base_pathname='{name}/'.format(name=url),
                assets_folder=get_root_path(__name__) + '{name}/assets/'.format(name=url),
                meta_tags=[meta_viewport],
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

        x.config.suppress_callback_exceptions = True
        return x


