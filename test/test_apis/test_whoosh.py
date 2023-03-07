from test.settings import client, read

import pandas as pd
import pandas.testing as pt

from pyweb.testing.response import get


def test_reference(client):
    response = get(client=client, url="/whoosh/json").data.decode()
    frame = read("whoosh.csv", index_col=0, header=0)[
        ["content", "group", "path", "title"]
    ]
    pt.assert_frame_equal(pd.read_json(
        response, orient="table")[frame.keys()], frame)


def test_app(client):
    get(client, url="/whoosh/json")
    get(client, url="/whoosh/html")
