from collections import namedtuple
from flask import Blueprint, render_template

LinkTuple = namedtuple('Link', ['href', 'text'])


def construct_navbar(links=None, version=None):
    blueprint = Blueprint('admin', __name__, template_folder="templates", static_folder="static")
    version = version or 0
    @blueprint.route('', methods=['GET'])
    def get_index():
        return render_template("index.html", links=links, version=version)

    return blueprint
