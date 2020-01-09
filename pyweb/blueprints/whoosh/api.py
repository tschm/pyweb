from flask import Blueprint, render_template
from pyweb.core.format import Format
from pyweb.core.parser import respond_pandas
from pyweb.core.whoosh import Whoosh

blueprint = Blueprint('whoosh_api', __name__, template_folder="templates")


@blueprint.route('/<fmt>', methods=['GET'])
def search(fmt):
    if Format.parse(fmt) == Format.HTML:
        return render_template("results.html")

    return respond_pandas(Whoosh.frame(), format=fmt)
