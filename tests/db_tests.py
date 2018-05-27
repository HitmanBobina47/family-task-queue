from family_task_queue import db
from flask import Flask
import tempfile

class Test_DB():
    def __init__(self):
        app = None

    def setup(self):
        app = Flask(__name__)
        _, temp_db = tempfile.mkstemp()
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{temp_db}"
        app.config["TESTING"] = True
        db.init_app(app)
        db.db.drop_all()
        db.db.create_all()

    def teardown(self):
        db.db.drop_all()

    def test_create_family(self):
        assert len(db.user.User.query.all()) == 0
        db.user.create_family("This Is A Test")
        assert len(db.user.User.query.all()) == 1
        assert db.user.User.query.first().name == "This Is A Test"
