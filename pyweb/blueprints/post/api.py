import json

from flask import Blueprint, request

from pyweb.web.highcharts import parse
from pyweb.web.parser import respond_pandas

blueprint = Blueprint("post", __name__, static_folder="static")


def __series():
    return parse(value=json.loads(request.data))
    # series is an array [[t1,v1],[t2,v2],...]


@blueprint.route("/performance", methods=["POST"])
def performance():
    returns = __series().pct_change()
    perf = returns.describe()
    perf = {key: f"{value:.2%}" for key, value in perf.to_dict().items()}
    perf["count"] = str(len(__series()))
    # print(perf.to_dict())
    print(perf)

    return respond_pandas(frame=perf, fmt="json")
