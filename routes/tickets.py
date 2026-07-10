from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db
from models.ticket import Ticket

tickets = Blueprint("tickets", __name__)

@tickets.route("/tickets")
@login_required
def my_tickets():

    tickets_list = Ticket.query.filter_by(
        user_id=current_user.id
    ).order_by(Ticket.id.desc()).all()

    return render_template(
        "tickets.html",
        tickets=tickets_list
    )

@tickets.route("/ticket/<int:ticket_id>")
@login_required
def view_ticket(ticket_id):

    ticket = Ticket.query.get_or_404(ticket_id)

    return render_template(
        "ticket_detail.html",
        ticket=ticket
    )


@tickets.route("/tickets/<int:ticket_id>/status/<status>")
@login_required
def update_status(ticket_id, status):

    ticket = Ticket.query.get_or_404(ticket_id)

    if ticket.user_id != current_user.id:
        flash("Unauthorized access.")
        return redirect(url_for("tickets.my_tickets"))

    allowed = ["Open", "In Progress", "Resolved"]

    if status not in allowed:
        flash("Invalid status.")
        return redirect(url_for("tickets.view_ticket", ticket_id=ticket.id))

    ticket.status = status

    db.session.commit()

    flash("Ticket updated successfully!")

    return redirect(url_for("tickets.view_ticket", ticket_id=ticket.id))

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
