from flask import Blueprint, request, render_template
from pyutil.sql.interfaces.whoosh import Whoosh
from pyweb.blueprints.whoosh.forms.forms import SearchForm
from pyweb.core.parser import respond_pandas
from pyweb.exts.exts import db

blueprint = Blueprint('whoosh_api', __name__, template_folder="templates")


@blueprint.route('/search', methods=['POST','GET'])
def search():
    form = SearchForm(search="CARMPAT FP Equity")
    if request.method == 'POST' and form.validate():
        return render_template("results.html", query=form.search.data)

    return render_template("search.html", form=form)


@blueprint.route('/index/<string:name>', methods=['GET'])
def get(name):
    results = db.session.query(Whoosh).filter(Whoosh.content.like(name)).all()
    return respond_pandas(Whoosh.frame(results), format="JSON")