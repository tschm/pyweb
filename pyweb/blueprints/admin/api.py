import os

from flask import Blueprint, render_template

version = os.getenv("VERSION", "0.0.0")

blueprint = Blueprint("admin", __name__, template_folder="templates", static_folder=None)


@blueprint.route("", methods=["GET"])
def index():
    return render_template("index.html", version=version)
