import json
import pytest
import pandas as pd

from pyutil.performance.return_series import from_nav
from pyutil.web.parser import HighchartsSeries
from pyutil.testing.aux import post
from test.settings import client, read

import pandas.util.testing as pdt


@pytest.fixture(scope="module")
def price():
    ts = read("price.csv", index_col=0, header=0, parse_dates=True)["A"]
    assert isinstance(ts, pd.Series)
    return ts


@pytest.fixture(scope="module")
def data(price):
    data = HighchartsSeries.to_json(series=price)
    assert data[0] == [1356998400000, 1673.78]
    return json.dumps(data)


def test_drawdown(client, data, price):
    d = json.loads(post(client=client, data=data, url="/api/1/engine/drawdown"))
    x = HighchartsSeries.parse(d)
    pdt.assert_series_equal(from_nav(price).drawdown, x, check_names=False)


def test_volatility(client, data, price):
    d = json.loads(post(client=client, data=data, url="/api/1/engine/volatility"))
    x = HighchartsSeries.parse(d)
    pdt.assert_series_equal(from_nav(price).ewm_volatility().dropna(), x, check_names=False)


def test_month(client, data, price):
    d = post(client=client, data=data, url="/api/1/engine/month")
    x = pd.read_json(d, orient="table")
    pdt.assert_frame_equal(x, from_nav(price).monthlytable.applymap(
        lambda x: "{0:.2f}%".format(float(100.0 * x)).replace("nan%", "")), check_names=False)


def test_performance(client, data):
    d = post(client=client, data=data, url="/api/1/engine/performance")
    x = pd.read_json(d, typ="series")

    assert x.to_dict() == {'Return': '-28.27%', '# Events': '602', '# Events per year': '261',
                           'Annua Return': '-14.40%', 'Annua Volatility': '18.01%',
                           'Annua Sharpe Ratio (r_f = 0)': '-0.80', 'Max Drawdown': '32.61%',
                           'Max % return': '4.07%', 'Min % return': '-9.11%', 'MTD': '1.43%',
                           'YTD': '1.33%', 'Current Nav': '1200.59', 'Max Nav': '1692.70',
                           'Current Drawdown': '29.07%', 'Calmar Ratio (3Y)': '-0.44',
                           '# Positive Events': '286', '# Negative Events': '316',
                           'Value at Risk (alpha = 95)': '1.91%',
                           'Conditional Value at Risk (alpha = 95)': '2.76%', 'First at': '2013-01-01',
                           'Last at': '2015-04-22', 'Kurtosis': '8.75'}
