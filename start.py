#!/usr/bin/env python3
from waitress import serve

from pyweb.application import create_app

from pyweb.exts.exts import db

from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
from pyweb.blueprints.post.api import blueprint as blue_post
from pyweb.blueprints.admin.api import blueprint as blue_ui


if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    print("Go to http://localhost:4445/admin")

    # This assert fails if we start with docker-compose.test.yml...
    # assert not app.config["TESTING"]
    app = create_app(extensions=[db])

    app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
    app.register_blueprint(blue_post, url_prefix="/api/1/engine")
    app.register_blueprint(blue_ui, url_prefix="/admin")

    serve(app=app, port=8000)
