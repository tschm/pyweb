
from pyweb.dash.pydash.callbacks import Cache
from test.settings import client, read
import pandas.util.testing as pdt


class TestCallbacks(object):
    def test_cache(self):
        prices = read("price.csv", index_col=0, parse_dates=True)
        x = Cache.to_json(frame=prices)
        pdt.assert_frame_equal(prices, Cache.frame(x), check_names=False)

