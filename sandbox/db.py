from flask import g, current_app
from pymssql import _mssql


def get_db():
    if 'db' not in g:
        g.db = _mssql.connect(server=current_app.config['DB_HOST'],
                              user=current_app.config['DB_USERNAME'],
                              password=current_app.config['DB_PASSWORD'],
                              database=current_app.config['DB_NAME'])

    return g.db
