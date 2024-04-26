from flask import abort, current_app, redirect, render_template, request, url_for
from flask_login import login_user
from app.models.users import Users
from . import auth_bp, helpers
from app.extensions import bcrypt, cache


@auth_bp.route("/")
@auth_bp.route("/checkpoint", methods=["GET", "POST"])
@cache.cached()
def user_checkpoint():
    """ Login Users to application """

    if request.method == "POST":
        user_data = dict(request.form)
        if not user_data:
            return render_template("register_and_login.html")

        user_record = Users.query.filter_by(
            email=user_data.get("email", None)
        ).first()

        if not user_record:
            # you can also use flash() to send notice message to users
            # i'm using choosing to log and abort but it's not the ideal way.
            current_app.logger.info("No user record found")
            abort(404, "Invalid username/password")

        if not bcrypt.check_password_hash(
            user_record.password, user_data["password"]
        ):
            current_app.logger.info("Invalid user name and password")
            abort(404, "Invalid username/password")

        current_app.logger.info("Before login_user")
        login_user(user_record)
        current_app.logger.info("after login_user")
        user_default_page = helpers.fetch_dashboard_url(user_record.role)
        next_url = request.args.get("next", None)
        all_urls = [endpoints.rule for endpoints in current_app.url_map.iter_rules()]
        if not helpers.is_safe_url(current_app, next_url):
            return redirect(user_default_page)

        return redirect(next_url or user_default_page)

    return render_template("register_and_login.html")
