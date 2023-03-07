import os

import pandas as pd
import pytest

from pyweb.app import create_app
from pyweb.blueprints.whoosh.whoosh import Whoosh


# resource is now a function mapping a name to a file in the resource folder
def read(name, **kwargs):
    return pd.read_csv(
        os.path.join(os.path.dirname(__file__), "resources", name), **kwargs
    )


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
