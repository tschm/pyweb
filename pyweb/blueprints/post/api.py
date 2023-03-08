import json

from flask import Blueprint, request
from pyutil.performance.return_series import from_nav

from pyweb.web.highcharts import parse, to_json
from pyweb.web.parser import respond_pandas

blueprint = Blueprint("post", __name__, static_folder="static")


def __percentage(x):
    return f"{100 * float(x):.2f}%".replace("nan%", "")


def __series():
    return from_nav(parse(value=json.loads(request.data)))
    # series is an array [[t1,v1],[t2,v2],...]


@blueprint.route("/performance", methods=["POST"])
def performance():
    perf = __series().summary_format().apply(str)
    return respond_pandas(frame=perf.to_dict(), fmt="json")


@blueprint.route("/month", methods=["POST"])
def month():
    # return a frame...
    return respond_pandas(
        frame=__series().monthlytable.applymap(__percentage), fmt="json"
    )


@blueprint.route("/drawdown", methods=["POST"])
def drawdown():
    return respond_pandas(frame=to_json(__series().drawdown), fmt="json")


@blueprint.route("/volatility", methods=["POST"])
def volatility():
    return respond_pandas(frame=to_json(__series().ewm_volatility()), fmt="json")
