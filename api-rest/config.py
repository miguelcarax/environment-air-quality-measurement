import os


class Config(object):
    """
        Environment configuration. Should be different for each environment
    """
    ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'very-secure-password'
    DB_SERVER = 'localhost'
    # SQLALCHEMY_DATABASE_URI = "postgresql://api:api@postgres/api"
    # SQLALCHEMY_DATABASE_URI = create_database_endpoint()
    # Supress deprecation Warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'postgresql://{}:{}@{}:{}/{}'.format(
            os.getenv('POSTGRES_API_USER'),
            os.getenv('POSTGRES_API_PASSWORD'),
            os.getenv('POSTGRES_HOST'),
            os.getenv('POSTGRES_PORT'),
            os.getenv('POSTGRES_API_SCHEMA')
        )
