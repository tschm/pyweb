import os
base_dir = os.path.dirname(__file__)

from flask import Blueprint, render_template

blueprint = Blueprint('ui', __name__, template_folder=os.path.join(base_dir, "templates"),
                      static_folder=os.path.join(base_dir, "static"))

@blueprint.route('/', methods=['GET'])
@blueprint.route('/index', methods=['GET'])
def get_index():
    return render_template("index.html")






