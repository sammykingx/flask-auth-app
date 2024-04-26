from flask import abort, current_app, redirect, render_template, url_for
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import BadTimeSignature, SignatureExpired
from app.extensions import bcrypt
from app.models.users import db, Users
from app.models import db_crud
from app.tasks import mail as mail_service
from . import auth_bp, helpers


@auth_bp.route("/request_reset_token/<user_email>")
def send_password_reset_token(user_email: str):
    """sends user email contain their password reset token"""

    user_record = db_crud.return_single_record(Users, email=user_email)
    if not user_record:
        abort(400, "Invalid email")

    token = helpers.pwd_reset_serializer.dumps(user_email)
    msg = render_template("emails/password_reset.html", token=token)
    task = mail_service.send_mail.delay(
            "Passowrd RESET - Scholar",
            user_record.email,
            msg
        )

    return "<h2>Check your registered mailbox to proceed, you're almost there.</h2>"


@auth_bp.route("/reset_password/<token>/<new_password>")
def reset_password(token: str, new_password: str = 1234567890):
    """verify's and activates user account"""

    try:
        email = helpers.pwd_reset_serializer.loads(token, max_age=1800)

    except SignatureExpired:
        abort(400, "verification token has expired")

    except BadTimeSignature:
        abort(400, "Invalid reset token")

    hashed_pwd = bcrypt.generate_password_hash(new_password)
    record = db_crud.return_single_record(Users, email=email)
    record.password = hashed_pwd

    db.session.commit()
    db.session.refresh(record)

    return f"<h2>Password Changed Successfully</h2>"
