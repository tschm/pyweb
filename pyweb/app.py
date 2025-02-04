from whitenoise import WhiteNoise

from .blueprints.admin.api import blueprint as blue_admin
from .blueprints.post.api import blueprint as blue_post
from .exts.exts import bootstrap, cache
from .web.application import create_server


def create_app():
    server = create_server(extensions=[cache, bootstrap], static_folder="/static")

    server.register_blueprint(blue_post, url_prefix="/engine")
    server.register_blueprint(blue_admin, url_prefix="/admin")

    # add whitenoise
    server.wsgi_app = WhiteNoise(server.wsgi_app, root="/static", prefix="/assets")

    return server
