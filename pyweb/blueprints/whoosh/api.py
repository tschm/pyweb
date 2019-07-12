from flask import Blueprint, render_template
from pyweb.core.format import Format
from pyweb.core.parser import respond_pandas
from pyweb.exts.exts import db
from pyweb.core.whoosh import Whoosh

blueprint = Blueprint('whoosh_api', __name__, template_folder="templates")


@blueprint.route('/<format>', methods=['GET'])
def search(format):
    if Format.parse(format) == Format.HTML:
        return render_template("results.html")

    results = db.session.query(Whoosh).all()
    return respond_pandas(Whoosh.frame(results), format=format)
