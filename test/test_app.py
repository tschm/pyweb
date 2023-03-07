# this is weird but this is needed...
import pytest

from pyweb.testing.response import get


def test_index(client):
    get(client, url="/admin")


def test_wrong_address(client):
    with pytest.raises(AssertionError):
        get(client, url="/I_dunno")
