from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_mail import Mail
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from . import app_limiter


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
mail = Mail()
cache = Cache()
limiter = Limiter(
        get_remote_address,
        default_limits = app_limiter.route_default_limits,
        storage_uri = app_limiter.storage_uri,
    )
