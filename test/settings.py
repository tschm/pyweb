import pandas as pd
from pyweb.app import create_app

# this is a function mapping name of a file to its path...
from pyutil.mongo.engine.whoosh import Whoosh


import os
base_dir = os.path.dirname(__file__)


def resource(name):
    return os.path.join(base_dir, "resources", name)


def read(name, **kwargs):
    return pd.read_csv(resource(name), **kwargs)


import pytest


def __init_session():
    Whoosh.objects.delete()

    w1 = Whoosh(title="A", content="AA", path="aaa", group="GA")
    w2 = Whoosh(title="B", content="BB", path="bbb", group="GB")
    w1.save()
    w2.save()


@pytest.fixture(scope="module")
def client():
    app = create_app()

    app.config['WTF_CSRF_METHODS'] = []  # This is the magic
    app.config['TESTING'] = True

    with app.app_context():
        __init_session()

    yield app.test_client()
