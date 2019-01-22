from flask import Blueprint, request, render_template
from flask_restplus import Api

from pyweb.blueprints.whoosh.forms.forms import SearchForm
from .whoosh import api as namespace

blueprint = Blueprint('whoosh_api', __name__, url_prefix='/api/1', template_folder="templates", static_url_path="/whoosh/static", static_folder="./static")

api = Api(blueprint,
    title='Lobnek RESTful API',
    version='1.0',
    description='Little RESTful API',
    doc='/documentation/whoosh'
)

api.add_namespace(namespace, path='')


@blueprint.route('/search', methods=['POST','GET'])
def search():
    form = SearchForm(search="CARMPAT FP Equity")
    if request.method == 'POST' and form.validate():
        return render_template("results.html", query=form.search.data)

    return render_template("search.html", form=form)



