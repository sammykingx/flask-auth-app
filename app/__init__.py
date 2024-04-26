from flask import Flask
from config.dev_config import DevelopmentConfig
from app.main import admin, users
from app.extensions import db, bcrypt, migrate, mail, cache, limiter
from app.extensions.login_system import login_manager
from app.tasks import celery_init_app
import app.auth, app.errors, os


def create_app(config_class: object = DevelopmentConfig) -> Flask:
    """flask application factory"""

    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    celery_init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(admin.admin_bp)
    app.register_blueprint(users.users_bp)

    app.register_error_handler(404, errors.not_found_error)
    # uncomment this when you've created a template for 500 error
    # in templates/errors
    # app.register_error_handler(500, errors.internal_server_error)

    return app
