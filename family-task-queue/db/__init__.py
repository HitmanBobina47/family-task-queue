from .db import *
import .task
import .user

def init_app(app):
    db.db.init_app(app)