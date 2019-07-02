import json
from flask import Blueprint, request, Response
from pyutil.performance.summary import fromNav

from pyweb.core.parser import HighchartsSeries

blueprint = Blueprint('post', __name__, static_folder="static")


def series():
    return fromNav(HighchartsSeries.parse(value=json.loads(request.data)))
    # series is an array [[t1,v1],[t2,v2],...]


@blueprint.route('/performance', methods=['POST'])
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

    x = perf.apply(str).to_json()
    return Response(x, mimetype="application/json")


@blueprint.route('/month', methods=['POST'])
def month():
    x = series().monthlytable.applymap(lambda x: "{0:.2f}%".format(float(100.0 * x)).replace("nan%", "")).to_json(
        orient="table")
    return Response(x, mimetype="application/json")


@blueprint.route('/drawdown', methods=['POST'])
def drawdown():
    x = json.dumps(HighchartsSeries.to_json(series().drawdown))
    return Response(x, mimetype="application/json")


@blueprint.route('/volatility', methods=['POST'])
def volatility():
    x = json.dumps(HighchartsSeries.to_json(series().ewm_volatility()))
    return Response(x, mimetype="application/json")
