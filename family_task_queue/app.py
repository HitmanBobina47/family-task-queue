from flask import Flask
from . import db

app = Flask(__name__)
db_path = os.path.join(tempfile.gettempdir(), "test.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TESTING"] = True

db.init_app(self.app)
db.db.drop_all(app=self.app)
db.db.create_all(app=self.app)

if __name__ == "__main__":
    with app.app_context():
        db.user.create_user("fatman")
    db.db.drop_all(app=self.app)
