from flask import current_app, url_for
from itsdangerous import URLSafeTimedSerializer
from dotenv import load_dotenv
import os


load_dotenv()
serializer_key = os.getenv("SERIALIZER_KEY")

email_confirmation_serializer = URLSafeTimedSerializer(
            serializer_key, salt="email_verification"
        )
pwd_reset_serializer = URLSafeTimedSerializer(
            serializer_key, salt="password_reset"
        )

def is_safe_url(app_instance: current_app, endpoint: str, is_https: bool = True) -> bool:
    """checks a url to prevent open redirects"""

    allowed_urls = [endpoints.rule for endpoints in app_instance.url_map.iter_rules()]
    if endpoint not in allowed_urls:
        return False

    if not is_https:
        return False

    return True


def fetch_dashboard_url(user_role) -> str:
    """returns the authenticated user dashbaord url"""

    if user_role == "user":
        return url_for("users.render_dashboard")

    elif user_role == "admin":
        return url_for("admin.render_dashboard")

    return url_for("index")
