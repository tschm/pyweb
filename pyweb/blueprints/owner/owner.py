import pandas as pd
from flask_restplus import Resource, Namespace, fields
from pyutil.sql.interfaces.risk.owner import Owner

from pyweb.core.decorators import csv, json
from pyweb.core.parser import HighchartsSeries #, Frame

api = Namespace('owner', description='Data for owners')

owner_field = api.model('Asset', {'name': fields.String, 'Nav': HighchartsSeries(description="A series")})


from pyweb.exts.exts import cache, db

@api.route('/reference/json')
class ReferenceJson(Resource):
    @cache.memoize()
    @json
    def get(self):
        # don't do this!
        owners = db.session.query(Owner)
        frame = Owner.frame(owners=owners).set_index("Name")
        return frame.to_json(orient="table")


@api.route('/reference/csv')
class ReferenceCsv(Resource):
    @cache.memoize()
    @csv
    def get(self):
        owners = db.session.query(Owner)
        frame = Owner.frame(owners=owners).set_index("Name")
        return frame.to_csv()


@api.route('/json/<string:name>')
@api.param('name', 'The name of the owner')
class OwnerJson(Resource):
    @api.marshal_with(owner_field)
    @cache.memoize()
    def get(self, name):
        return db.session.query(Owner).filter(Owner.name==name).one().to_json()


@api.route('/csv/<string:name>')
@api.param('name', 'The name of the owner')
class OwnerCsv(Resource):
    @csv
    @cache.memoize()
    def get(self, name):
        return pd.DataFrame(db.session.query(Owner).filter(Owner.name==name).one().to_json()).to_csv()


@api.route('/position/json/<string:name>')
@api.param('name', 'The name of the owner')
class OwnerPositionJson(Resource):
    @json
    @cache.memoize()
    def get(self, name):
        frame = db.session.query(Owner).filter(Owner.name==name).one().position_frame
        frame = frame.reset_index(drop=False)

        frame = frame.groupby(by=["Security", "Custodian"])["Date", "Position"].last()
        frame = frame.reset_index(drop=False)

        frame["Security"] = frame["Security"].apply(lambda x: x.name)
        frame["Custodian"] = frame["Custodian"].apply(lambda x: x.name)

        frame = frame.set_index(keys=["Date", "Custodian", "Security"])
        print(frame)

        return frame.to_json(orient="table")


@api.route('/position/csv/<string:name>')
@api.param('name', 'The name of the owner')
class OwnerPositionCsv(Resource):
    @json
    @cache.memoize()
    def get(self, name):
        # here we don't filter!
        return db.session.query(Owner).filter(Owner.name==name).one().position().to_csv()

