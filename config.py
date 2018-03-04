import os

class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5002
    HOST = '127.0.0.1'
    SERVER_NAME = '127.0.0.1:5003'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/dbflask'