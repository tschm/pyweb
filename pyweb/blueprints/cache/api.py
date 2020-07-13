from flask import Blueprint, render_template, current_app

blueprint = Blueprint('cache_api', __name__, template_folder="templates", static_folder=None)


def get(address, server="/api/1", client=None):
    client = client or current_app.test_client()
    response = client.get("{server}/{address}".format(server=server, address=address))
    assert response.status_code == 200, "The return code is {r} with {a}".format(r=response.status_code, a=address)

@blueprint.route("/refresh/data", methods=['GET'])
def refresh_data():
    raise NotImplementedError()

@blueprint.route("/refresh", methods=['GET'])
def refresh():
    return render_template("cache.html")

