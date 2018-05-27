from .db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey("family.id"), nullable=False)
    family = db.relationship("Family", backref=db.backref('members', lazy=True))
    roles = db.Column(db.PickleType(), nullable=False)


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
