from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_mongoengine import MongoEngine

cache = Cache()
engine = MongoEngine()
bootstrap = Bootstrap()
