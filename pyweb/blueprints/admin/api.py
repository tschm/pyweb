from flask import Blueprint, render_template

blueprint = Blueprint('admin', __name__, template_folder="templates", static_folder="static")

@blueprint.route('', methods=['GET'])
def get_index():
    return render_template("index.html")






