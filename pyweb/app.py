from flask import current_app, url_for

from pyutil.web.application import create_server
from pyweb.blueprints.admin.api import construct_navbar, LinkTuple
from pyweb import __version__ as version
from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.exts.exts import engine, cache
from whitenoise import WhiteNoise

def create_app():
    server = create_server(extensions=[engine, cache], static_folder="/static")

    with server.test_request_context():
        current_app.register_blueprint(blue_whoosh, url_prefix="/whoosh")
        current_app.register_blueprint(blue_post, url_prefix="/engine")
        # links
        links = [LinkTuple(href=url_for("whoosh.search", fmt="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(links=links, version=version), url_prefix="/admin")

    # add whitenoise
    server.wsgi_app = WhiteNoise(server.wsgi_app, root='/static', prefix='assets/')

    return server