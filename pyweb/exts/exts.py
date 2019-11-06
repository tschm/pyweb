from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
#Flask-PyMongo
from flask_pymongo import PyMongo

db = SQLAlchemy()
cache = Cache()
mongo = PyMongo()



