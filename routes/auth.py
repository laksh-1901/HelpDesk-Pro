from flask_login import login_user
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models.user import User
from extensions import db

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        if User.query.filter_by(username=username).first():

            flash("Username already exists")

            return redirect(url_for("auth.register"))

        if User.query.filter_by(email=email).first():

            flash("Email already exists")

            return redirect(url_for("auth.register"))

        user = User(
            username=username,
            email=email
        )

        user.set_password(password)

        db.session.add(user)

        db.session.commit()

        flash("Registration successful!")

        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):

            login_user(user)

            flash("Login Successful!")

            return redirect(url_for("dashboard"))

        flash("Invalid username or password")

    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.")

    return redirect(url_for("auth.login"))
