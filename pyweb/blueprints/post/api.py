import json
import pandas as pd
from flask import Blueprint, request
from pyutil.performance.summary import fromNav, NavSeries
from pyutil.web.parser import HighchartsSeries, respond_pandas

blueprint = Blueprint('post', __name__, static_folder="static")


def __percentage(x):
    return "{0:.2f}%".format(100*float(x)).replace("nan%", "")


def __series():
    value = json.loads(request.data)
    print(value)
    # check that is an array...
    assert isinstance(HighchartsSeries.parse(value), pd.Series)
    x = fromNav(HighchartsSeries.parse(value=json.loads(request.data)))
    assert isinstance(x, NavSeries)
    return x

    # series is an array [[t1,v1],[t2,v2],...]


@blueprint.route('/performance', methods=['POST'])
def performance():
    perf = __series().summary_format().apply(str)
    return respond_pandas(object=perf.to_dict(), format="json")


@blueprint.route('/month', methods=['POST'])
def month():
    # return a frame...
    return respond_pandas(object=__series().monthlytable.applymap(__percentage), format="json")


@blueprint.route('/drawdown', methods=['POST'])
def drawdown():
    return respond_pandas(object=HighchartsSeries.to_json(__series().drawdown), format="json")


@blueprint.route('/volatility', methods=['POST'])
def volatility():
    a = __series()
    assert isinstance(a, NavSeries)
    b = a.ewm_volatility()
    assert isinstance(b, pd.Series)
    return respond_pandas(object=HighchartsSeries.to_json(__series().ewm_volatility()), format="json")
