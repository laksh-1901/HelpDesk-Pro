from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from models.user import User
from models.ticket import Ticket

admin = Blueprint("admin", __name__)


@admin.route("/admin")
@login_required
def dashboard():

    if current_user.role != "admin":
        flash("Access denied.")
        return redirect(url_for("dashboard"))

    search = request.args.get("search", "")

    status = request.args.get("status", "")

    priority = request.args.get("priority", "")

    query = Ticket.query

    if search:
        query = query.filter(Ticket.title.contains(search))

    if status:
        query = query.filter(Ticket.status == status)

    if priority:
        query = query.filter(Ticket.priority == priority)

    tickets = query.order_by(Ticket.created_at.desc()).all()

    return render_template(
        "admin_dashboard.html",
        total_users=User.query.count(),
        total_tickets=Ticket.query.count(),
        open_tickets=Ticket.query.filter_by(status="Open").count(),
        progress_tickets=Ticket.query.filter_by(status="In Progress").count(),
        resolved_tickets=Ticket.query.filter_by(status="Resolved").count(),
        tickets=tickets
    )
