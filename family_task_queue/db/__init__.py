from . import db, task, user
from db import *

def init_app(app):
    db.db.init_app(app)
