from flask import current_app, flash, redirect, render_template, request, url_for
from flask_mail import Message
from flask_login import login_user
from app.extensions import bcrypt
from app.models.users import db, Users
from app.models import db_crud
from app.tasks import mail as mail_service
from . import auth_bp, helpers


@auth_bp.route("/register", methods=["POST"])
def register_user():
    """user registration endpoint"""

    user_data = dict(request.form)
    res = db_crud.return_single_record(Users, email=user_data.get("email", None))
    if res:
       flash("kindly loggin")
       return redirect(url_for("auth.user_checkpoint"))

    user_data["password"] = bcrypt.generate_password_hash(
        user_data["password"]
    )
    user_data.update(role="user", is_verified=False)
    record = db_crud.save_record(Users, **user_data)
    token = helpers.email_confirmation_serializer.dumps(user_data["email"])
    msg = render_template("emails/email_verification.html", token=token)
    task = mail_service.send_mail.delay(
            "Account Activation",
            user_data["email"],
            msg
        )
    login_user(record)
    return redirect(url_for("users.render_dashboard"))
