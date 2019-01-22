import os
base_dir = os.path.dirname(__file__)

from flask import Blueprint
from flask_restplus import Api

from .post import api as post

blueprint = Blueprint('post', __name__, static_folder=os.path.join(base_dir, "static"))

api = Api(blueprint,
    title='Lobnek RESTful API',
    version='1.0',
    description='Little RESTful API',
    doc='/documentation'
)

api.add_namespace(post, path='')