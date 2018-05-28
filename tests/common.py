from flask import Flask
import tempfile, os
from family_task_queue import db

def create_app():
    app = Flask(__name__)
    db_path = os.path.join(tempfile.gettempdir(), "test.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["TESTING"] = True
    db.init_app(app)
    db.db.drop_all(app=app)
    db.db.create_all(app=app)
    return app

def create_user_and_family(**kwargs):
    kwargs2 = {
        "first_name": "Fatso",
        "last_name": "McGatso",
        "family": "Mongowski"
    }
    db.user.create_family(kwargs2["family"])
    kwargs2.update(kwargs)
    db.user.create_user(
        "fatsomcgatso",
        "password",
        "ex@amp.le",
        **kwargs2
    )
