from dotenv import load_dotenv
import os


load_dotenv()


class DevelopmentConfig:
    """all app configurations"""

    DEBUG = True
    
    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")

    MAIL_SERVER = os.getenv("SMTP_HOST")
    MAIL_PORT = os.getenv("SMTP_PORT")
    #MAIL_USE_TLS = bool(os.getenv("USE_TLS"))
    MAIL_USE_SSL = bool(os.getenv("USE_SSL"))
    MAIL_USERNAME = os.getenv("SMTP_MAIL")
    MAIL_PASSWORD = os.getenv("SMTP_PWD")
    MAIL_DEFAULT_SENDER = os.getenv("SMTP_MAIL") or "your_mail@mail_provider.com"

    CACHE_TYPE = "FileSystemCache"
    CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24 * 10 # caching for 10 days
    CACHE_DIR = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "app_cache"
        )
    CACHE_THRESHOLD = 100
