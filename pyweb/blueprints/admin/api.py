from flask import Blueprint, render_template
from pyweb import __version__ as version

blueprint = Blueprint('admin', __name__, template_folder="templates", static_folder=None)

# You can override the templates... with the central templates of the application
@blueprint.route('', methods=['GET'])
def get_index():
    return render_template("index.html", version=version)
