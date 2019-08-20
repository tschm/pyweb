from flask import Flask

from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.blueprints.admin.api import blueprint as blue_ui

def create_app(static_folder="static", template_folder="templates", extensions=None):
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    success = app.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    for extension in extensions:
        extension.init_app(app)

    app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
    app.register_blueprint(blue_post, url_prefix="/api/1/engine")
    app.register_blueprint(blue_ui, url_prefix="/admin")


    return app

