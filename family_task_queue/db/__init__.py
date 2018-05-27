from . import task, user, db as _db
from .db import *

def init_app(app):
    db.init_app(app)
