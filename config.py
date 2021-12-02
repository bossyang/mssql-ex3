from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    DB_HOST = "localhost"
    DB_NAME = environ.get('MSSQL_DATABASE')
    DB_USERNAME = "sa"
    DB_PASSWORD = environ.get('MSSQL_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    DEVELOPMENT = True
