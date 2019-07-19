import json
from flask import Blueprint, request, Response
from pyutil.performance.summary import fromNav
from pyutil.portfolio.format import percentage

from pyweb.core.parser import HighchartsSeries

blueprint = Blueprint('post', __name__, static_folder="static")


def series():
    return fromNav(HighchartsSeries.parse(value=json.loads(request.data)))
    # series is an array [[t1,v1],[t2,v2],...]


@blueprint.route('/performance', methods=['POST'])
def performance():
    perf = series().summary_format()
    return Response(perf.to_json(), mimetype="application/json")


@blueprint.route('/month', methods=['POST'])
def month():
    x = (100*series().monthlytable).applymap(percentage).to_json(orient="table")
    return Response(x, mimetype="application/json")


@blueprint.route('/drawdown', methods=['POST'])
def drawdown():
    x = json.dumps(HighchartsSeries.to_json(series().drawdown))
    return Response(x, mimetype="application/json")


@blueprint.route('/volatility', methods=['POST'])
def volatility():
    x = json.dumps(HighchartsSeries.to_json(series().ewm_volatility()))
    return Response(x, mimetype="application/json")
