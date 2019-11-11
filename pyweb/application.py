from flask import Flask, current_app


def create_server(static_folder="static", template_folder="templates", extensions=None):
    server = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    if not extensions:
        extensions = []

    success = server.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    with server.app_context():
        for extension in extensions:
            extension.init_app(current_app)

    return server
