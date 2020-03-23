from flask import Blueprint, render_template
from pyutil.web.parser import respond_pandas
from pyweb.blueprints.whoosh.whoosh import Whoosh

blueprint = Blueprint('whoosh_api', __name__, template_folder="templates")


@blueprint.route('/<fmt>', methods=['GET'])
def search(fmt):
    if fmt.lower().strip() == "html":
        return render_template("results.html")

    return respond_pandas(Whoosh.frame(), format=fmt)
