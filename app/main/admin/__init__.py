from flask import Blueprint

admin_bp = Blueprint(
        "admin",
        __name__,
        url_prefix="/admin",
        static_folder="static",
    )

from . import dashboard, profile
