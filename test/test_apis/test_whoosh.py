import pandas as pd
import pandas.util.testing as pdt
from pyutil.testing.aux import get
from test.settings import read, client


class TestWhoosh(object):

    def test_reference(self, client):
        response = get(client=client, url="/api/1/whoosh/json")
        frame = read("whoosh.csv", index_col=0, header=0)[["content", "group", "path", "title"]]
        pdt.assert_frame_equal(pd.read_json(response, orient="table")[frame.keys()], frame)

    def test_app(self, client):
        get(client, url="/api/1/whoosh/json")
        get(client, url="/api/1/whoosh/html")
