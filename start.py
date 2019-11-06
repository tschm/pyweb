#!/usr/bin/env python3
from flask import current_app, url_for
from waitress import serve

from pyweb.application import create_server
from pyweb.blueprints.admin.api import LinkTuple, construct_navbar
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.exts.exts import db, mongo
from pyweb import __verion__ as version

if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    print("Go to http://localhost:4445/admin")

    # This assert fails if we start with docker-compose.test.yml...
    # assert not app.config["TESTING"]

    server = create_server(extensions=[db])

    with server.test_request_context():
        current_app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
        current_app.register_blueprint(blue_post, url_prefix="/api/1/engine")

        links = [LinkTuple(href=url_for("whoosh_api.search", format="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(links=links, version=version), url_prefix="/admin")

    serve(app=server, port=8000)
