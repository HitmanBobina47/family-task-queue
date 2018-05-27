from family_task_queue import db
from flask import Flask
import tempfile, os

class Test_DB():
    def __init__(self):
        app = None

    def setup(self):
        self.app = Flask(__name__)
        db_path = os.path.join(tempfile.gettempdir(), "test.db")
        self.app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
        self.app.config["TESTING"] = True
        db.init_app(self.app)
        db.db.drop_all(app=self.app)
        db.db.create_all(app=self.app)

    def teardown(self):
        db.db.drop_all(app=self.app)

    def test_create_family(self):
        with self.app.app_context():
            assert len(db.user.Family.query.all()) == 0
            db.user.create_family("This Is A Test")
            assert len(db.user.Family.query.all()) == 1
            assert db.user.User.query.first().name == "This Is A Test"
