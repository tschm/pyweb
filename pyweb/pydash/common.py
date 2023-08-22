# Meta tags for viewport responsiveness
import uuid
from abc import ABCMeta, abstractmethod
from collections import namedtuple

from dash import Dash
from flask.helpers import get_root_path

style = {"width": "96%", "display": "inline-block", "padding": 10}

AppTuple = namedtuple("App", ["dash", "href", "text"])

# don't delete; every app can use this functionality


class App(Dash):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # only store the name of the function here, do not call build_layout()!
        self.layout = self.build_layout
        # register the callbacks
        self.register_callback()

        # create the handler here...
        # self.__handler = DashLogger(
        #    fmt="[%(asctime)s] %(levelname)s: %(message)s")
        # self.__handler.setLevel(logging.DEBUG)

    @abstractmethod
    def build_layout(self):
        raise NotImplementedError()

    @abstractmethod
    def register_callback(self):
        raise NotImplementedError()

    @classmethod
    def dash_application(cls, url=None):
        # Create a Dash app
        meta_viewport = {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
        }
        url = url or "/" + uuid.uuid4()

        dash_app = cls(
            name=cls.__name__,
            server=False,
            url_base_pathname=f"{url}/",
            assets_folder=get_root_path(__name__) + f"{url}/assets/",
            meta_tags=[meta_viewport],
            external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"],
            eager_loading=True,
        )

        dash_app.config.suppress_callback_exceptions = True
        return dash_app
