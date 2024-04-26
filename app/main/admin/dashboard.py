from flask import abort, render_template
from flask_login import login_required, current_user
from . import admin_bp
from app.models.users import Users
from app.models import db_crud


@admin_bp.route("/panel")
@login_required
def render_dashboard():
    """renders admin dashboard"""

    if current_user.role != "admin":
        abort(401, "Unauthorised access to resource")

    return render_template("dashboard.html")
