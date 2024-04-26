from flask import abort, current_app, flash, render_template
from itsdangerous.exc import BadTimeSignature, SignatureExpired
from app.models.users import db, Users
from app.models import db_crud
from . import auth_bp, helpers


@auth_bp.route("/email_verification/<token>")
def email_verification(token: str):
    """verify's and activates user account"""

    # see how you can use the serializer in one app only
    #serializer = URLSafeTimedSerializer(
    #        current_app.config["SECRET_KEY"], salt="email_verification"
    #    )

    try:
        email = helpers.email_confirmation_serializer.loads(token, max_age=1800)

    except SignatureExpired:
        abort(400, "verification token has expired")

    except BadTimeSignature:
        abort(400, "Bad Signature")

    record = db_crud.return_single_record(Users, email=email)
    record.is_verified = True

    db.session.commit()
    db.session.refresh(record)

    return f"<h2>All good, Email Verified</h2>"
