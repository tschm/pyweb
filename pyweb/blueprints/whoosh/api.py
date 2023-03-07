from flask import Blueprint, render_template

from pyweb.blueprints.whoosh.whoosh import Whoosh
from pyweb.web.parser import respond_pandas

blueprint = Blueprint(
    "whoosh", __name__, template_folder="templates", static_folder="static"
)


@blueprint.route("/<fmt>", methods=["GET"])
def search(fmt):
    if fmt.lower().strip() == "html":
        return render_template("results.html")

    return respond_pandas(Whoosh.frame(), format=fmt)
