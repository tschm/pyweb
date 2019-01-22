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


# def test_portfolio():
#     return _Portfolio(prices=read("price.csv", index_col=0, header=0, parse_dates=True),
#                       weights=read("weight.csv", index_col=0, header=0, parse_dates=True))

def __session():
    return postgresql_db_test(Base).session


def __init_session(session):

    # p = test_portfolio()
    #
    # symbols = {asset: Symbol(name=asset, group=SymbolType.fixed_income) for asset in p.assets}
    #
    # # add all symbols to session
    # session.add_all(symbols.values())
    # session.commit()
    #
    # strat = Strategy(name="test", source="Peter Maffay")
    #
    # strat.upsert(portfolio=p, symbols=symbols)
    # session.add(strat)
    # session.commit()
    #
    # s1 = Symbol(name="Symbol A", group=SymbolType.alternatives)
    # s2 = Symbol(name="Symbol B", group=SymbolType.equities)
    # session.add_all([s1, s2])
    # session.commit()
    #
    # f1 = Field(name="Field A", result=DataType.string)
    # f2 = Field(name="Field B", result=DataType.string)
    # session.add_all([f1, f2])
    # session.commit()
    #
    # s1.reference[f1] = "Peter"
    # s2.reference[f2] = "Maffay"
    #
    # prices = read(__resource("price.csv"), index_col=0, parse_dates=True, header=0)
    # for key in prices.keys():
    #     s = session.query(Symbol).filter_by(name=key).one()
    #     s.upsert_price(ts=prices[key].dropna())

    w1 = Whoosh(title="a", content="a", path="c", group="d")
    session.add(w1)

    session.commit()

    return session


@pytest.fixture(scope="module")
def client():
    from pyweb.blueprints.whoosh.api import blueprint as blue_whoosh
    from pyweb.blueprints.post.api import blueprint as blue_post
    from pyweb.blueprints.ui.ui import blueprint as blue_ui

    assert base_dir == "/pyweb/test", "Base directory is {f}".format(f=base_dir)

    static_folder = os.path.join(base_dir, "static")
    template_folder = os.path.join(base_dir, "templates")

    class A(Application):
        @property
        def blueprints(self):
            return [blue_whoosh, blue_post, blue_ui]

        @property
        def extensions(self):
            return [db, csrf_protect]

    app = create_app(A(), static_folder=static_folder, template_folder=template_folder)
    app.config['WTF_CSRF_METHODS'] = []  # This is the magic
    app.config['TESTING'] = True
    with app.app_context():
        db.session = __session()
        __init_session(session=db.session)

    yield app.test_client()
    db.session.close()


def read(name, **kwargs):
    return pd.read_csv(__resource(name), **kwargs)
