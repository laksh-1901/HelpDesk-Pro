from flask_login import login_required, current_user
from flask import Flask
from flask_login import login_required, current_user
from config import Config
from extensions import db, login_manager
from models.user import User
from extensions import db, login_manager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from models import *
from routes.auth import auth

app.register_blueprint(auth)

@app.route("/")
@login_required
def dashboard():

    return f"""
    <h2>Welcome, {current_user.username}!</h2>

    <p>Role: {current_user.role}</p>

    <a href="/logout">Logout</a>
    """

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
