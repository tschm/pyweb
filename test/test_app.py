import pytest

from pyutil.testing.aux import get
from test.settings import client


class TestApp(object):
    def test_index(self, client):
        get(client, url="/admin")
        get(client, url="/api/1/whoosh/html")
        get(client, url="/api/1/whoosh/json")

    def test_wrong_address(self, client):
        with pytest.raises(AssertionError):
            get(client, url="/I_dunno")
