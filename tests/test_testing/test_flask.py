import pandas.testing as pt
import pytest

from pyweb.testing.response import get, post, response2csv, response2json
from tests.test_testing.server import app, frame


@pytest.fixture(scope="module")
def client():
    app.config["TESTING"] = True
    yield app.test_client()


def test_get(client):
    data = get(client, url="/hello").data
    assert data.decode() == "Hello World!"


def test_post(client):
    data = post(client, url="/post", data={}).data
    assert data.decode() == "Hello Thomas!"


def test_csv(client):
    f = response2csv(get(client, url="/csv"), index_col=0)
    pt.assert_frame_equal(f, frame)


def test_json(client):
    f = response2json(get(client, url="/json"), orient="table")
    pt.assert_frame_equal(f, frame)
