from datetime import datetime

from extensions import db


class Ticket(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    priority = db.Column(db.String(20), nullable=False)

    status = db.Column(db.String(20), default="Open")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", backref="tickets")
