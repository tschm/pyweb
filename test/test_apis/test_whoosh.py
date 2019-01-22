from unittest import mock
from attrdict import AttrDict

import pandas as pd
import pandas.util.testing as pdt
from pyutil.testing.aux import get, post
from test.settings import read, client


class TestWhoosh(object):

    def test_reference(self, client):
        response = get(client=client, url="/api/1/whoosh/whoosh/index/a")
        pdt.assert_frame_equal(pd.read_json(response, orient="table")[["content","group","path","title"]], read("whoosh.csv", index_col=0, header=0))

    def test_app(self, client):
        get(client, url="/api/1/whoosh/whoosh/index/a")
        get(client, url="/api/1/whoosh/search")

    # def test_form(self, client):
    #     with client:
    #         x = SearchForm(search="Hans")
    #         assert x.validate()
    #         assert x.search.data == "Hans"


    def test_post(self, client):
        class NewForm(object):
            def validate(self):
                return True
            search = AttrDict({"data": "Hans"})

        # -- obsolete code to cross check NewForm...
        x = NewForm()
        assert x.validate()
        assert x.search.data == "Hans"

        with mock.patch("pyweb.blueprints.whoosh.forms.forms.SearchForm") as MockForm:
            MockForm.return_value = NewForm()
            post(client, url="/api/1/whoosh/search", data=None)

