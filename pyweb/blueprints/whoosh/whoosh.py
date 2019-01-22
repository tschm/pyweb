from flask_restplus import Resource, Namespace

from pyweb.core.decorators import json
from pyweb.exts.exts import db

api = Namespace('whoosh', description='Index')

from pyutil.sql.interfaces.whoosh import Whoosh

@api.route('/index/<string:name>')
@api.param('name', 'Whoosh name')
class WhooshApi(Resource):
    @json
    def get(self, name):
        results = db.session.query(Whoosh).filter(Whoosh.content.like(name)).all()
        return Whoosh.frame(results).to_json(orient="table")
