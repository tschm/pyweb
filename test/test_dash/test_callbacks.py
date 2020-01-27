from pyweb.pydash.pydash.callbacks import Cache
from test.settings import read
import pandas.util.testing as pdt


def test_cache():
    prices = read("price.csv", index_col=0, parse_dates=True)
    x = Cache.to_json(frame=prices)
    pdt.assert_frame_equal(prices, Cache.read_json(x), check_names=False)

