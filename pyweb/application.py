from flask import Flask


def create_app(static_folder="static", template_folder="templates", extensions=None):
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    success = app.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    for extension in extensions:
        extension.init_app(app)

    return app

