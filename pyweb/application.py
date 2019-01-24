from flask import Flask

from pyweb.exts.exts import db

from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.blueprints.admin.api import blueprint as blue_ui


def extensions():
    return [db]


def create_app():
    app = Flask(__name__)

    success = app.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    for extension in extensions():
        extension.init_app(app)

    app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
    app.register_blueprint(blue_post, url_prefix="/api/1/engine")
    app.register_blueprint(blue_ui, url_prefix="/admin")

    print(app.url_map)

    return app

