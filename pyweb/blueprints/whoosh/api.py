from flask import Blueprint, request, render_template
from pyweb.blueprints.whoosh.forms.forms import SearchForm
from pyweb.core.decorators import json
from pyweb.exts.exts import db
from pyutil.sql.interfaces.whoosh import Whoosh

blueprint = Blueprint('whoosh_api', __name__, template_folder="templates", static_folder="static")

@blueprint.route('/search', methods=['POST','GET'])
def search():
    form = SearchForm(search="CARMPAT FP Equity")
    if request.method == 'POST' and form.validate():
        return render_template("results.html", query=form.search.data)

    return render_template("search.html", form=form)


@blueprint.route('/index/<string:name>', methods=['GET'])
@json
def get(name):
    results = db.session.query(Whoosh).filter(Whoosh.content.like(name)).all()
    return Whoosh.frame(results).to_json(orient="table")
