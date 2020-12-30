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
