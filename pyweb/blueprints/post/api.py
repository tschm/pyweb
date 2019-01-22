from flask import Blueprint
from flask_restplus import Api

from .post import api as post

blueprint = Blueprint('post_api', __name__, url_prefix='/api/1')

api = Api(blueprint,
    title='Lobnek RESTful API',
    version='1.0',
    description='Little RESTful API',
    doc='/documentation'
)

api.add_namespace(post, path='')