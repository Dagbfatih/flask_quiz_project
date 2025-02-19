from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from src.server.models.user import User

auth_api_bp = Blueprint("auth_api", __name__)


@auth_api_bp.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        full_name = request.form["full_name"]
        password = request.form["password"]

        user = User.query.filter_by(full_name=full_name).first()
        if user and user.check_password(password):  # Direct password comparison
            login_user(user)
            return redirect(url_for("index.home"))
        else:
            flash("Login failed. Check username and/or password.", "danger")

    return render_template("pages/login.html")


@auth_api_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
