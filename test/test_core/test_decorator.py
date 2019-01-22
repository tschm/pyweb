from io import StringIO

import pandas as pd
import pandas.util.testing as pdt
import pytest

from pyweb.core.decorators import csv, json

@pytest.fixture
def nav():
    return pd.Series({pd.Timestamp('2014-12-11'): 1.29, pd.Timestamp('2014-12-12'): 1.29, pd.Timestamp('2014-12-15'): 1.28})


def test_csv(nav):
    @csv
    def f():
        return nav.to_csv()

    pdt.assert_series_equal(pd.read_csv(StringIO(f().data.decode("utf-8")), index_col=0, squeeze=True, header=None, parse_dates=True), nav, check_names=False)

def test_json(nav):
    @json
    def f():
        return nav.to_json()

    pdt.assert_series_equal(pd.read_json(f().data, typ="series"), nav, check_names=False)

