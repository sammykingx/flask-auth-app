from flask import Blueprint


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    static_folder="static",
)

from . import (
        checkpoint,
        user_signin,
        admin_sign_up,
        verify_email,
        forgot_password,
        logout,
    )
