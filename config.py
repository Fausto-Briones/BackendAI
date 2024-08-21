import os

class Config:
    # Basic Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_secure_secret_key'
    
    # Database configuration (if you're using a database)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy event system

    # Other possible configurations
    # Flask-Mail settings
    # MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Caching (e.g., with Redis)
    # CACHE_TYPE = "redis"
    # CACHE_DEFAULT_TIMEOUT = 300

    # API keys (if your app interacts with external APIs)
    # SOME_API_KEY = os.environ.get('SOME_API_KEY')

    # Debug mode (only for development, should be False in production)
    DEBUG = True
