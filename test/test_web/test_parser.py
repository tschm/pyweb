import json
from io import StringIO

import pandas as pd
import pandas.testing as pt
import pytest

from pyweb.web.parser import respond_pandas


@pytest.fixture
def nav():
    return pd.Series(
        {
            pd.Timestamp("2014-12-11"): 1.29,
            pd.Timestamp("2014-12-12"): 1.29,
            pd.Timestamp("2014-12-15"): 1.28,
        }
    )


def test_respond_frame_json(nav):
    x = nav.to_frame(name="Maffay")
    response = respond_pandas(x, "json")
    pt.assert_frame_equal(pd.read_json(
        response.data, typ="frame", orient="table"), x)


def test_respond_json():
    x = ["A", "B"]
    assert json.loads(respond_pandas(x, "json").data) == x


def test_respond_frame_csv(nav):
    x = nav.to_frame(name="Maffay")
    response = respond_pandas(x, "csv")
    f = pd.read_csv(
        StringIO(response.data.decode("utf-8")), index_col=0, header=0, parse_dates=True
    )
    pt.assert_frame_equal(f, x, check_names=False)
