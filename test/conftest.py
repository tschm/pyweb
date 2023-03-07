import os
from pathlib import Path

import pytest

from pyweb.app import create_app


@pytest.fixture(scope="session", name="resource_dir")
def resource_fixture():
    """resource fixture"""
    return Path(__file__).parent / "resources"

@pytest.fixture(scope="module")
def application_settings(resource_dir):
    os.environ["APPLICATION_SETTINGS"] = str(resource_dir / "settings.cfg")

@pytest.fixture(scope="module")
def client(application_settings):
    #os.environ["APPLICATION_SETTINGS"] = str(resource_dir / "settings.cfg")
    app = create_app()
    yield app.test_client()
