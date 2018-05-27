from .db import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    family = db.relationship("Family", backref=db.backref('tasks', lazy=True))
    family_id = db.Column(db.Integer, db.ForeignKey("family.id"), nullable=False)
    author = db.relationship("User", backref=db.backref('created_tasks', lazy=True))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    incentives = db.Column(db.PickleType(), nullable=False)
    time_limit = db.Column(db.DateTime(), nullable=False)

def create_task(name, family, author, incentives=None, time_limit=None):
    pass

