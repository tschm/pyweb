import os

from pyweb.testing.response import get
from test.settings import client


def test_files():
    assert os.path.exists("/static/css/custom.css")
    assert os.path.exists("/static/img/logo.png")
    assert os.path.exists("/static/ico/favicon.ico")


def test_index(client):
    get(client, url="/assets/css/custom.css")
    get(client, url="/assets/img/logo.png")
    get(client, url="/assets/ico/favicon.ico")
