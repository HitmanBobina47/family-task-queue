from family_task_queue.frontend import auth
from common import create_app, create_user_and_family

class Test_Frontend_Auth():
    def __init__(self):
        self.app = None

    def setup(self):
        self.app = create_app()
        auth.init_app(self.app)

    def test_load_user(self):
        with self.app.app_context():
            create_user_and_family(first_name="test_load_user")
            user = auth.load_user(1)
            assert user is not None
            assert user.first_name == "test_load_user"
