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

    # API Backend config
    BACKEND_HOST = os.getenv('BACKEND_HOST')
    BACKEND_PORT = os.getenv('BACKEND_PORT')

    # Redis configuration
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
