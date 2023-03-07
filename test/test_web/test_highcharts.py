import pandas as pd
import pandas.testing as pt

from pyweb.web.highcharts import parse, to_json


def test_parser():
    nav = pd.Series(
        {
            pd.Timestamp("2014-12-11"): 1.29,
            pd.Timestamp("2014-12-12"): 1.29,
            pd.Timestamp("2014-12-15"): 1.28,
        }
    )
    pt.assert_series_equal(parse(to_json(nav)), nav)
