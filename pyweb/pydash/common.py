# Meta tags for viewport responsiveness
from abc import ABCMeta, abstractmethod
from collections import namedtuple

from flask.helpers import get_root_path

from pyweb.pydash.pydash.dash_util import build_app

style = {'width': '96%', 'display': 'inline-block', 'padding': 10}

AppTuple = namedtuple('App', ['dash', 'href', 'text'])

# don't delete; every app can use this functionality
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Output, Input, State
import dash_table



class App(object):
    __metaclass__ = ABCMeta

    def __init__(self, app=None):
        self.__app = app or build_app(name=__name__)
        self.__app.layout = self.layout
        self.register_callback()

    @property
    def app(self):
        return self.__app

    @abstractmethod
    def register_callback(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def layout(self):
        raise NotImplementedError()

    @property
    def server(self):
        return self.__app.server

    def serve(self):
        from waitress import serve
        print("http://localhost:8050")
        serve(app=self.server, port=8050)

    @classmethod
    def construct_with_flask(cls, server, url):
        meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

        return cls(app=dash.Dash(__name__,
                                 server=server,
                                 url_base_pathname='{name}/'.format(name=url),
                                 assets_folder=get_root_path(__name__) + '{name}/assets/'.format(name=url),
                                 meta_tags=[meta_viewport],
                                 external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']))
