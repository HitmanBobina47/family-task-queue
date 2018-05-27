import .db
import .task

def init_app(app):
    db.db.init_app(app)
