import os
base_dir = os.path.dirname(__file__)

from flask import Blueprint, render_template

blueprint = Blueprint('ui', __name__, template_folder=os.path.join(base_dir, "templates"), static_url_path="/ui/static",
                      static_folder=os.path.join(base_dir, "static"))

@blueprint.route('/', methods=['GET'])
@blueprint.route('/index', methods=['GET'])
def get_index():
    print(blueprint.template_folder)
    assert False
    return render_template("index.html")






