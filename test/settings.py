import pandas as pd

from pyutil.sql.base import Base
from pyutil.testing.aux import resource_folder, postgresql_db_test
from pyutil.sql.interfaces.whoosh import Whoosh

import pytest

# this is a function mapping name of a file to its path...
from pyweb.application import create_app, Application
from pyweb.exts.exts import db, csrf_protect

import os
base_dir = os.path.dirname(__file__)

__resource = resource_folder(folder=base_dir)


def __session():
    return postgresql_db_test(Base).session

def __init_session(session):
    w1 = Whoosh(title="a", content="a", path="c", group="d")
    session.add(w1)

    session.commit()

    return session


@pytest.fixture(scope="module")
def client():
    from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
    from pyweb.blueprints.post.api import blueprint as blue_post
    from pyweb.blueprints.admin.api import blueprint as blue_ui

    assert base_dir == "/pyweb/test", "Base directory is {f}".format(f=base_dir)

    static_folder = os.path.join(base_dir, "static")
    template_folder = os.path.join(base_dir, "templates")

    class A(Application):
        @property
        def extensions(self):
            return [db, csrf_protect]

    app = create_app(A(), static_folder=static_folder, template_folder=template_folder)
    app.config['WTF_CSRF_METHODS'] = []  # This is the magic
    app.config['TESTING'] = True
    with app.app_context():
        db.session = __session()
        __init_session(session=db.session)

    app.register_blueprint(blue_whoosh, url_prefix="/api/1/whoosh")
    app.register_blueprint(blue_post, url_prefix="/api/1/engine")
    app.register_blueprint(blue_ui, url_prefix="/admin")

    print(app.url_map)

    yield app.test_client()
    db.session.close()


def read(name, **kwargs):
    return pd.read_csv(__resource(name), **kwargs)
