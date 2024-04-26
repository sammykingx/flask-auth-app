#from flask import render_template
from flask_login import login_required
from . import admin_bp


@admin_bp.route("/profile")
@login_required
def render_admin_profile():
    """renders admin profile"""

    return f"<h2>Here's the admin profile page</h2>"
