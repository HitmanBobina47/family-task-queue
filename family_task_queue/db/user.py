from .db import db, add_item
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    family = db.relationship("Family", backref=db.backref('members', lazy=True))
    family_id = db.Column(db.Integer, db.ForeignKey("family.id"), nullable=False)
    roles = db.Column(db.PickleType(), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

def get_family(arg):
    if isinstance(arg, int):
        return Family.query.get(arg)
    elif isinstance(arg, Family):
        return arg
    elif isinstance(arg, str):
        return Family.query.filter_by(name=arg).first()

def create_family(name):
    new_family = Family(name=name)
    add_item(new_family)

def create_user(username, password, email, family=None, first_name=None, last_name=None):
    family = get_family(family)
    new_user = User(
        username=username,
        password=pbkdf2_sha256.hash(password),
        email=email,
        family=family,
        family_id=family.id,
        roles={},
        first_name=first_name,
        last_name=last_name
    )
    add_item(new_user)
