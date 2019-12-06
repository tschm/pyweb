import pandas as pd
from flask import current_app

from pyutil.sql.base import Base
from pyutil.testing.aux import resource_folder
from pyutil.testing.database import database

from pyweb.app import create_app

# this is a function mapping name of a file to its path...
from pyweb.core.whoosh import Whoosh
from pyweb.exts.exts import db, mongo, cache

import os
base_dir = os.path.dirname(__file__)

__resource = resource_folder(folder=base_dir)

import pytest


def __init_session(session):
    w1 = Whoosh(title="A", content="AA", path="aaa", group="GA")
    w2 = Whoosh(title="B", content="BB", path="bbb", group="GB")
    session.add_all([w1,w2])
    session.commit()
    return session


@pytest.fixture(scope="module")
def client():
    app = create_app()

    app.config['WTF_CSRF_METHODS'] = []  # This is the magic
    app.config['TESTING'] = True

    with app.app_context():
        db.session = database(Base).session
        __init_session(session=db.session)

    yield app.test_client()
    db.session.close()


def read(name, **kwargs):
    return pd.read_csv(__resource(name), **kwargs)
