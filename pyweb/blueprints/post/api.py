from flask import Blueprint, request
import json as jj
import pandas as pd
from pyutil.performance.summary import fromNav
from pyweb.core.decorators import json

blueprint = Blueprint('post', __name__, static_folder="static")

def to_json(series):
    return [[int(pd.Timestamp(t).value * 1e-6), float(value)] for t, value in series.dropna().items()]

def series():
    def parse(value):
        return pd.Series({pd.Timestamp(1e6 * int(v[0])): float(v[1]) for v in value})

    data = jj.loads(request.data)
    assert isinstance(data, list)

    return fromNav(parse(data))
    # series is an array [[t1,v1],[t2,v2],...]

@blueprint.route('/performance', methods=['POST'])
@json
def performance():
    perf = series().summary()

    f = lambda x: "{0:.2f}%".format(float(x))
    for name in ["Return", "Annua Return", "Annua Volatility", "Max Drawdown", "Max % return", "Min % return",
                 "MTD", "YTD", "Current Drawdown", "Value at Risk (alpha = 95)",
                 "Conditional Value at Risk (alpha = 95)"]:
        perf[name] = f(perf[name])

    f = lambda x: "{0:.2f}".format(float(x))
    for name in ["Annua Sharpe Ratio (r_f = 0)", "Calmar Ratio (3Y)", "Current Nav", "Max Nav"]:
        perf[name] = f(perf[name])

    f = lambda x: "{:d}".format(int(x))
    for name in ["# Events", "# Events per year", "# Positive Events", "# Negative Events"]:
        perf[name] = f(perf[name])

    return perf.apply(str).to_json()


@blueprint.route('/month', methods=['POST'])
@json
def month():
    return series().monthlytable.applymap(lambda x: "{0:.2f}%".format(float(100.0 * x)).replace("nan%", "")).to_json(orient="table")

@blueprint.route('/drawdown', methods=['POST'])
@json
def drawdown():
    return jj.dumps(to_json(series().drawdown))

@blueprint.route('/volatility', methods=['POST'])
@json
def volatility():
    return jj.dumps(to_json(series().ewm_volatility()))
