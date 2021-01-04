import os


class Config(object):
    """
    This configuration should be overwritten for production environments
    """
    # Flask app configuration
    ENV = 'development'
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'very-secure-password'
    # Suppress deprecation Warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database configuration for SQLAlchemy
    DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        os.getenv('POSTGRES_API_USER'),
        os.getenv('POSTGRES_API_PASSWORD'),
        os.getenv('POSTGRES_HOST'),
        os.getenv('POSTGRES_PORT'),
        os.getenv('POSTGRES_API_SCHEMA')
    )
