from family_task_queue import db
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from common import create_app, create_user_and_family

def create_user_impl(family="Mongowski"):
    create_user_and_family(family=family)

def create_user_assert(family_name):
    first = db.user.User.query.first()
    assert first.username == "fatsomcgatso"
    assert pbkdf2_sha256.verify("password", first.password)
    assert first.email == "ex@amp.le"
    assert first.family.name == family_name
    assert first.first_name == "Fatso"
    assert first.last_name == "McGatso"

class Test_DB():
    def __init__(self):
        self.app = None

    def setup(self):
        self.app = create_app()

    def teardown(self):
        pass

    def test_create_family(self):
        with self.app.app_context():
            starting_len = len(db.user.Family.query.all())
            db.user.create_family("This Is A Test")
            assert len(db.user.Family.query.all()) == starting_len + 1
            assert db.user.Family.query.first().name == "This Is A Test"

    def test_get_family(self):
        with self.app.app_context():
            starting_len = len(db.user.Family.query.all())
            db.user.create_family("This Is A Test")
            assert len(db.user.Family.query.all()) == starting_len + 1
            assert db.user.get_family(1).name == "This Is A Test"
            assert db.user.get_family("This Is A Test").name == "This Is A Test"
            assert db.user.get_family(db.user.Family.query.first()).name == "This Is A Test"

    def test_create_user_family_id(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            starting_len = len(db.user.User.query.all())
            create_user_impl(family=1)
            assert len(db.user.User.query.all()) == starting_len + 1
            create_user_assert("Mongowski")

    def test_create_user_family(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            starting_len = len(db.user.User.query.all())
            create_user_impl(family=db.user.Family.query.filter_by(name="Mongowski").first())
            assert len(db.user.User.query.all()) == starting_len + 1
            create_user_assert("Mongowski")

    def test_create_user_family_name(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            starting_len = len(db.user.User.query.all())
            create_user_impl(family="Mongowski")
            assert len(db.user.User.query.all()) == starting_len + 1
            create_user_assert("Mongowski")

    def test_get_user(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            create_user_impl(family="Mongowski")
            assert db.user.get_user(1).username == "fatsomcgatso"
            assert db.user.get_user("fatsomcgatso").username == "fatsomcgatso"
            assert db.user.get_user(db.user.User.query.first()).username == "fatsomcgatso"


    def test_create_task(self):
        with self.app.app_context():
            db.user.create_family("Mongowski")
            create_user_impl(family="Mongowski")
            db.task.create_task("Take out the trash", "Mongowski", "fatsomcgatso", incentives=[], time_limit=datetime.now())
            assert db.task.Task.query.get(1).name == "Take out the trash"
            assert db.task.Task.query.get(1).family.name == "Mongowski"
            assert db.task.Task.query.get(1).author.username == "fatsomcgatso"
            assert len(db.task.Task.query.get(1).incentives) == 0
