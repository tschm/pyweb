#!/usr/bin/env python3
from waitress import serve

from flask import current_app, url_for

from pyutil.web.application import create_server
from pyweb.blueprints.admin.api import construct_navbar, LinkTuple
from pyweb import __version__ as version
from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.exts.exts import engine, cache


def create_app():
    server = create_server(extensions=[engine, cache])

    with server.test_request_context():
        # register the blueprint
        current_app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
        current_app.register_blueprint(blue_post, url_prefix="/api/1/engine")
        # links
        links = [LinkTuple(href=url_for("whoosh_api.search", fmt="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(links=links, version=version), url_prefix="/admin")

    return server


if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    print("Go to http://localhost:4445/admin")

    # This assert fails if we start with docker-compose.test.yml...
    # assert not app.config["TESTING"]
    server = create_app()

    serve(app=server, port=8000)
