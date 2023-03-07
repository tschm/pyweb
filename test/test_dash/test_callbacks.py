from test.settings import read

import pandas.testing as pt

from pyweb.pydash.pydash.callbacks import Cache


def test_cache():
    prices = read("price.csv", index_col=0, parse_dates=True)
    x = Cache.to_json(frame=prices)
    pt.assert_frame_equal(prices, Cache.read_json(x), check_names=False)
