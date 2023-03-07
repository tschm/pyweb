import os
from pathlib import Path

import pytest

from pyweb.app import create_app


@pytest.fixture(scope="session", name="resource_dir")
def resource_fixture():
    """resource fixture"""
    return Path(__file__).parent / "resources"


@pytest.fixture(scope="module")
def client(resource_dir):
    os.environ["APPLICATION_SETTINGS"] = str(resource_dir / "settings.cfg")
    # def __init_session():
    #    Whoosh.objects.delete()
    #    Whoosh(title="A", content="AA", path="aaa", group="GA").save()
    #    Whoosh(title="B", content="BB", path="bbb", group="GB").save()

    app = create_app()

    # with app.app_context():
    #    __init_session()

    yield app.test_client()
