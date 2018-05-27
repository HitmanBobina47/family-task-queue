from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def add_item(item):
    db.session.add(item)
    db.session.commit()
