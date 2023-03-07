# this is weird but this is needed...
from test.settings import client

import pytest

from pyweb.testing.response import get


def test_index(client):
    get(client, url="/admin")
    get(client, url="/whoosh/html")
    get(client, url="/whoosh/json")


def test_wrong_address(client):
    with pytest.raises(AssertionError):
        get(client, url="/I_dunno")
