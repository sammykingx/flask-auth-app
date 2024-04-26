from flask import Blueprint

users_bp = Blueprint(
        "users",
        __name__,
        url_prefix="/users",
        static_folder="static",
    )

from . import dashboard
