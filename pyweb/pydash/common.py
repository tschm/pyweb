# Meta tags for viewport responsiveness
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


class App(Dash):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = self.build_layout()

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
