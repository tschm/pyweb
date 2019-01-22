from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
cache = Cache()
csrf_protect = CSRFProtect()