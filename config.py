from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = '9f83a6fc859ab7e532e2b27cfec2123c1a84689935151587d84294df63cc008d'
    DB_HOST = environ.get('MSSQL_HOSTNAME')
    DB_NAME = environ.get('MSSQL_DATABASE')
    DB_USERNAME = environ.get('MSSQL_USERNAME')
    DB_PASSWORD = environ.get('MSSQL_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    DEVELOPMENT = True
