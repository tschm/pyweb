import pytest

from pyutil.testing.response import get
# this is weird but this is needed...
from test.settings import client


def test_index(client):
    get(client, url="/admin")
    get(client, url="/api/1/whoosh/html")
    get(client, url="/api/1/whoosh/json")


def test_wrong_address(client):
    with pytest.raises(AssertionError):
        get(client, url="/I_dunno")
