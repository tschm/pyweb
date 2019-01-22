from flask import Blueprint, render_template

blueprint = Blueprint('ui', __name__, template_folder="templates", static_url_path="/ui/static", static_folder="./static")

@blueprint.route('/', methods=['GET'])
@blueprint.route('/index', methods=['GET'])
def get_index():
    return render_template("index.html")






