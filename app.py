from flask import Flask, render_template
from flask_login import login_required, current_user

from config import Config
from extensions import db, login_manager
from routes.admin import admin

from models.user import User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from routes.auth import auth
from routes.tickets import tickets
from models.ticket import Ticket

app.register_blueprint(auth)
app.register_blueprint(tickets)
app.register_blueprint(admin)

@app.route("/")
@login_required
def dashboard():

    total = Ticket.query.filter_by(user_id=current_user.id).count()

    open_tickets = Ticket.query.filter_by(
        user_id=current_user.id,
        status="Open"
    ).count()

    return render_template(
        "dashboard.html",
        total=total,
        open_tickets=open_tickets
    )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
