from flask import Blueprint
from flask_login import LoginManager
from family_task_queue.db.user import get_user

bp = Blueprint('auth', __name__, url_prefix="/auth")
login_manager = LoginManager()

def init_app(app):
    app.register_blueprint(bp)

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

@bp.route("/register", methods=["GET", "POST"])
def register():
    pass
