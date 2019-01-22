from flask import Blueprint, render_template
from flask_restplus import Api

from .security import api as namespace

blueprint = Blueprint('security_api', __name__, url_prefix='/api/1', template_folder="templates", static_url_path="/security/static", static_folder="./static")

api = Api(blueprint,
    title='Lobnek RESTful API',
    version='1.0',
    description='Little RESTful API',
    doc='/documentation/asset'
)

api.add_namespace(namespace, path="")

@blueprint.route('/securities', methods=['GET'])
def get_securities_html():
    return render_template("securities_dynamic.html")

@blueprint.route('/prices', methods=['GET'])
def get_prices_html():
    return render_template("prices.html")


@blueprint.route('/security/<name>', methods=['GET'])
def get_security_html(name):
    return render_template("security.html", name=name)