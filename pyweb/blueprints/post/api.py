import json
from flask import Blueprint, request, Response
from pyutil.performance.summary import fromNav
from pyweb.core.parser import HighchartsSeries

blueprint = Blueprint('post', __name__, static_folder="static")


def __percentage(x):
    return "{0:.2f}%".format(100*float(x)).replace("nan%", "")


def __series():
    return fromNav(HighchartsSeries.parse(value=json.loads(request.data)))
    # series is an array [[t1,v1],[t2,v2],...]


@blueprint.route('/performance', methods=['POST'])
def performance():
    perf = __series().summary_format().apply(str)
    return Response(perf.to_json(), mimetype="application/json")


@blueprint.route('/month', methods=['POST'])
def month():
    x = __series().monthlytable.applymap(__percentage).to_json(orient="table")
    return Response(x, mimetype="application/json")


@blueprint.route('/drawdown', methods=['POST'])
def drawdown():
    x = json.dumps(HighchartsSeries.to_json(__series().drawdown))
    return Response(x, mimetype="application/json")


@blueprint.route('/volatility', methods=['POST'])
def volatility():
    x = json.dumps(HighchartsSeries.to_json(__series().ewm_volatility()))
    return Response(x, mimetype="application/json")
