from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db
from models.ticket import Ticket

tickets = Blueprint("tickets", __name__)


@tickets.route("/tickets")
@login_required
def my_tickets():

    ticket_list = Ticket.query.filter_by(user_id=current_user.id).order_by(Ticket.created_at.desc()).all()

    return render_template("tickets.html", tickets=ticket_list)


@tickets.route("/tickets/create", methods=["GET", "POST"])
@login_required
def create_ticket():

    if request.method == "POST":

        ticket = Ticket(
            title=request.form["title"],
            description=request.form["description"],
            priority=request.form["priority"],
            user_id=current_user.id
        )

        db.session.add(ticket)
        db.session.commit()

        flash("Ticket created successfully!")

        return redirect(url_for("tickets.my_tickets"))

    return render_template("create_ticket.html")
