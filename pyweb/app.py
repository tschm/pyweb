#!/usr/bin/env python3
import os

from flask import current_app

from pyweb.application import create_server
from pyweb.blueprints.admin.api import construct_navbar
from pyweb.exts.exts import db
from pyweb import __verion__ as version

base_dir = os.path.dirname(__file__)


def create_app():
    server = create_server(static_folder=os.path.join(base_dir, "static"),
                           template_folder=os.path.join(base_dir, "templates"),
                           extensions=[db])

    with server.test_request_context():
        #print(url_for("whoosh_api.search", fmt="html"))

        #links = [LinkTuple(href=url_for("whoosh_api.search", fmt="html"), text="Search")]
        current_app.register_blueprint(construct_navbar(version=version), url_prefix="/admin")

    return server

