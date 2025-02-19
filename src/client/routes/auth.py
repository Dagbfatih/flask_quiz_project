from flask import Blueprint, render_template
from flask_login import logout_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login')
def login():
    return render_template('pages/login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    