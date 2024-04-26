from flask import abort, render_template
from flask_login import current_user, login_required
from . import users_bp


@users_bp.route("/dashboard")
@login_required
def render_dashboard():
    """renders users dashboard"""

    if current_user.role != "user":
        abort(401, "Unauthorised access to resource")

    return f"<h2>The User Dashboard</h2>"
