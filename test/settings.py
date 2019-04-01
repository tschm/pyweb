import pandas as pd

from pyutil.sql.base import Base
from pyutil.testing.aux import resource_folder, postgresql_db_test
from pyutil.sql.interfaces.whoosh import Whoosh


# this is a function mapping name of a file to its path...
from pyweb.application import create_app
from pyweb.exts.exts import db

import os
base_dir = os.path.dirname(__file__)

__resource = resource_folder(folder=base_dir)

import pytest

def __session():
    return postgresql_db_test(Base).session


def __init_session(session):
    w1 = Whoosh(title="a", content="a", path="c", group="d")
    session.add(w1)
    session.commit()
    return session


@pytest.fixture(scope="module")
def client():
    app = create_app()
    app.config['WTF_CSRF_METHODS'] = []  # This is the magic
    app.config['TESTING'] = True

    with app.app_context():
        db.session = __session()
        __init_session(session=db.session)

    yield app.test_client()
    db.session.close()


def read(name, **kwargs):
    return pd.read_csv(__resource(name), **kwargs)
