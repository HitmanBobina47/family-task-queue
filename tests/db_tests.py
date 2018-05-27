from family_task_queue import db
from flask import Flask
from passlib.hash import pbkdf2_sha256
import tempfile, os

class Test_DB():
    def __init__(self):
        app = None

    def setup(self):
        self.app = Flask(__name__)
        db_path = os.path.join(tempfile.gettempdir(), "test.db")
        self.app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
            assert db.user.Family.query.first().name == "This Is A Test"

    def test_create_user_family_id(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            assert len(db.user.User.query.all()) == 0
            db.user.create_user("fatsomcgatso", "password", "ex@amp.le", family_id=1)
            assert len(db.user.User.query.all()) == 1
            first = db.user.User.query.first()
            assert first.username == "fatsomcgatso"
            assert pbkdf2_sha256.verify("password", first.password)
            assert first.email == "ex@amp.le"
            assert first.family_id == 1
            assert first.family.name == "Mongowski"

    def test_create_user_family(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            assert len(db.user.User.query.all()) == 0
            db.user.create_user("fatsomcgatso", "password", "ex@amp.le", family=db.user.Family.query.filter_by(name="Mongowski").first())
            assert len(db.user.User.query.all()) == 1
            first = db.user.User.query.first()
            assert first.username == "fatsomcgatso"
            assert pbkdf2_sha256.verify("password", first.password)
            assert first.email == "ex@amp.le"
            assert first.family_id == 1
            assert first.family.name == "Mongowski"
