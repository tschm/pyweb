import pandas as pd
import pandas.util.testing as pdt

from pyweb.core.parser import HighchartsSeries
import pytest


@pytest.fixture
def nav():
    return pd.Series({pd.Timestamp('2014-12-11'): 1.29, pd.Timestamp('2014-12-12'): 1.29, pd.Timestamp('2014-12-15'): 1.28})


def test_parser(nav):
    pdt.assert_series_equal(HighchartsSeries.parse(HighchartsSeries.to_json(nav)), nav)

def test_parser_init():
    x = HighchartsSeries(description="Series")
    assert x.description == "Series"
