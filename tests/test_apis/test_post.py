import json

import pandas as pd
import pytest

from pyweb.testing.response import post
from pyweb.web.highcharts import to_json


@pytest.fixture(scope="module")
def price(resource_dir):
    ts = pd.read_csv(resource_dir / "price.csv", index_col=0, header=0, parse_dates=True)["A"]
    assert isinstance(ts, pd.Series)
    return ts


@pytest.fixture(scope="module")
def data(price):
    data = to_json(series=price)
    assert data[0] == [1356998400000, 1673.78]
    return json.dumps(data)


def test_performance(client, data):
    d = post(client=client, data=data, url="/engine/performance").data.decode()
    x = pd.read_json(d, typ="series")
    print(x)
    assert x.to_dict() == {
        "count": "602",
        "mean": "-0.05%",
        "std": "1.12%",
        "min": "-9.11%",
        "25%": "-0.52%",
        "50%": "-0.04%",
        "75%": "0.59%",
        "max": "4.07%",
    }
