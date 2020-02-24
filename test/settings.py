import pytest
import os
import pandas as pd


from flask import current_app, url_for

from pyutil.web.application import create_server
from pyweb.blueprints.admin.api import construct_navbar, LinkTuple
from pyweb import __version__ as version
from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.exts.exts import engine, cache


def create_app():
    server = create_server(extensions=[engine, cache])

    with server.test_request_context():
        # register the blueprint
        current_app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
        current_app.register_blueprint(blue_post, url_prefix="/api/1/engine")
        # links
        links = [LinkTuple(href=url_for("whoosh_api.search", fmt="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(links=links, version=version), url_prefix="/admin")

    return server

# this is a function mapping name of a file to its path...
from pyutil.mongo.engine.whoosh import Whoosh


# resource is now a function mapping a name to a file in the resource folder
def read(name, **kwargs):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "resources", name), **kwargs)


def __init_session():
    Whoosh.objects.delete()
    Whoosh(title="A", content="AA", path="aaa", group="GA").save()
    Whoosh(title="B", content="BB", path="bbb", group="GB").save()


@pytest.fixture(scope="module")
def client():
    app = create_app()

    with app.app_context():
        __init_session()

    yield app.test_client()
