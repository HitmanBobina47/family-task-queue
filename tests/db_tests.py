from family-task-queue import db
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
