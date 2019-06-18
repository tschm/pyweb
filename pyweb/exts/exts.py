from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_pymongo import PyMongo
from pyutil.mongo.mongo import Collection

db = SQLAlchemy()
cache = Cache()
mongo = PyMongo()


def mongo_collection(name):
    return Collection(collection=mongo.db[name])
