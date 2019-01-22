import pandas as pd
from flask_restplus import Resource, Namespace, fields
from pyutil.sql.interfaces.risk.security import Security

from pyweb.blueprints.security.data import prices
from pyweb.core.decorators import csv, json
from pyweb.core.parser import HighchartsSeries

api = Namespace('security', description='Data for securities')

asset_field = api.model('Asset', {'name': fields.String, 'Price': HighchartsSeries(description="A series")})

from pyweb.exts.exts import cache, db


@api.route('/reference/json')
class ReferenceJson(Resource):
    @json
    @cache.memoize()
    def get(self):
        securities = db.session.query(Security).all()
        frame = Security.frame(securities=securities).set_index("Name")
        return frame.to_json(orient="table")


@api.route('/reference/csv')
class ReferenceCsv(Resource):
    @cache.memoize()
    @csv
    def get(self):
        securities = db.session.query(Security).all()
        frame = Security.frame(securities=securities).set_index("Name")
        return frame.to_csv()

@api.route('/json/<string:name>')
@api.param('name', 'The name of the security')
class SecurityJson(Resource):
    @api.marshal_with(asset_field)
    @cache.memoize()
    def get(self, name):
        return db.session.query(Security).filter(Security.name == name).one().to_json()


@api.route('/csv/<string:name>')
@api.param('name', 'The name of the security')
class SecurityCsv(Resource):
    @csv
    @cache.memoize()
    def get(self, name):
        return pd.DataFrame(db.session.query(Security).filter(Security.name==name).one().to_json()).to_csv()


@api.route('/prices/csv')
class Prices(Resource):
    @csv
    @cache.memoize()
    def get(self):
        securities = db.session.query(Security).all()
        frame = prices(securities=securities)
        frame = frame.sort_index(ascending=False).stack().swaplevel()
        frame.index.names = ["Owned ID", "Date"]
        return frame.to_frame("Price").to_csv()


@api.route('/prices/json')
class Prices(Resource):
    @json
    @cache.memoize()
    def get(self):
        securities = db.session.query(Security).all()
        frame = prices(securities=securities)
        frame = frame.sort_index(ascending=False).head(50).stack().swaplevel()
        #print(frame)
        #frame = frame.sort_index(ascending=False).stack().swaplevel()
        frame.index.names = ["Owned ID", "Date"]
        return frame.to_frame("Price").to_json(orient="table")

