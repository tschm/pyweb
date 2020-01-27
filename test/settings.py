import pytest
import os
import pandas as pd

from pyweb.app import create_app

# this is a function mapping name of a file to its path...
from pyutil.mongo.engine.whoosh import Whoosh


# resource is now a function mapping a name to a file in the resource folder
def read(name, **kwargs):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), "resources", name), **kwargs)


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
