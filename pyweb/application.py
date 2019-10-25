from flask import Flask, url_for, current_app

from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.blueprints.admin.api import construct_navbar, LinkTuple


def create_app(server=None, static_folder="static", template_folder="templates", extensions=None):
    server = server or create_server(static_folder=static_folder, template_folder=template_folder, extensions=extensions)

    with server.test_request_context():
        current_app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
        current_app.register_blueprint(blue_post, url_prefix="/api/1/engine")

        links = [LinkTuple(href=url_for("whoosh_api.search", format="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(links=links), url_prefix="/admin")

    return server


def create_server(static_folder="static", template_folder="templates", extensions=None):
    server = Flask(__name__, static_folder=static_folder, template_folder=template_folder)
    server.logger.info("Server created using Flask: {s}".format(s=server))

    success = server.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    server.logger.info("Configuration: \n{c}".format(c=server.config))

    with server.app_context():
        for extension in extensions:
            extension.init_app(current_app)
            server.logger.info("Extension: \n{e}".format(e=extension))

    return server
