from flask import redirect, url_for
from flask_login import login_required, logout_user
from . import auth_bp


@auth_bp.route("/logout")
@login_required
def user_logout():
    logout_user()
    return redirect(url_for("index"))
