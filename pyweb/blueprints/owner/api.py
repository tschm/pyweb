from flask import Blueprint, render_template
from flask_restplus import Api

from .owner import api as namespace

blueprint = Blueprint('owner_api', __name__, url_prefix='/api/1', template_folder="templates", static_url_path="/owner/static", static_folder="./static")

api = Api(blueprint,
    title='Lobnek RESTful API',
    version='1.0',
    description='Little RESTful API',
    doc='/documentation/asset'
)

api.add_namespace(namespace, path="")

@blueprint.route('/owners', methods=['GET'])
def get_owners_html():
    return render_template("owners_dynamic.html")

@blueprint.route('/owner/<name>', methods=['GET'])
def get_owner_html(name):
    return render_template("owner.html", name=name)
