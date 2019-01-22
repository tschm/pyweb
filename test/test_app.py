import pytest

from pyutil.testing.aux import get
from test.settings import client


class TestApp(object):
    def test_index(self, client):
    #     # The get method is checking the correct response code
        #print(client.url_map)
        get(client, url="/index")
        get(client, url="/")
    #     get(client, url="/api/1/assets")
    #     get(client, url="/api/1/asset/A")
    #     get(client, url="/api/1/recently")
    #     get(client, url="/api/1/mtd")
    #     get(client, url="/api/1/ytd")
    #     get(client, url="/api/1/sector")
    #     get(client, url="/api/1/strategy/test")
    #     #get(client, url="/api/1/owner/200")
    #     #get(client, url="/api/1/security/500")

    def test_wrong_address(self, client):
        with pytest.raises(AssertionError):
            get(client, url="/I_dunno")
