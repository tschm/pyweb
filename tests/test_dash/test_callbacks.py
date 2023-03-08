import pandas as pd
import pandas.testing as pt

from pyweb.pydash.pydash.callbacks import Cache


def test_cache(resource_dir):
    prices = pd.read_csv(resource_dir / "price.csv",
                         index_col=0, parse_dates=True)
    x = Cache.to_json(frame=prices)
    pt.assert_frame_equal(prices, Cache.read_json(x), check_names=False)
