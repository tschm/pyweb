#!/usr/bin/env python3
import os

from flask import current_app, url_for

from pyweb.application import create_server
from pyweb.blueprints.admin.api import construct_navbar, LinkTuple
from pyweb.exts.exts import db
from pyweb import __verion__ as version
from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh

base_dir = os.path.dirname(__file__)


def create_app():
    server = create_server(static_folder=os.path.join(base_dir, "static"),
                           template_folder=os.path.join(base_dir, "templates"),
                           extensions=[db])

    with server.test_request_context():
        # register the blueprint
        current_app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")

        # you have to register the blueprint before you use the url_for...
        print(url_for("whoosh_api.search", fmt="html"))

        # links
        links = [LinkTuple(href=url_for("whoosh_api.search", fmt="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(links=links, version=version), url_prefix="/admin")

    return server

