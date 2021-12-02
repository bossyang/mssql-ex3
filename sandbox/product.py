from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
# from flaskr.auth import login_required
from sandbox.db import get_db


bp = Blueprint('product', __name__)


@bp.route('/')
def index():
    sqlcmd = 'SELECT * FROM CurrentProductInformation'
    conn = get_db()
    conn.execute_query(sqlcmd)
    return render_template('product/index.html', products=conn)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        error = None

        if not name:
            error = 'Name is required.'

        if not price:
            error = 'Price is required.'

        if error is not None:
            flash(error)
        else:
            sqlcmd = """
            EXEC usp_AddProduct %s,%d
            """
            conn = get_db()
            conn.execute_query(sqlcmd, (name, price))
            return redirect(url_for('product.index'))

    return render_template('product/create.html')


def get_product(id):
    sqlcmd = """
    SELECT * FROM CurrentProductInformation WHERE ProductId = %d
    """
    conn = get_db()
    product = conn.execute_row(sqlcmd, (id))

    if product is None:
        abort(404, f"Product id {id} doesn't exist.")

    return product


@bp.route('/<int:id>/update', methods=('GET', 'POST'))

def update(id):
    product = get_product(id)

    if request.method == 'POST':
        price = request.form['price']
        start_date = request.form['start_date']
        error = None

        if not price:
            error = 'Price is required.'

        if not start_date:
            error = 'Start date is required.'

        if error is not None:
            flash(error)
        else:
            sqlcmd = """
            EXEC usp_UpdateProduct %s,%s,%d
            """
            conn = get_db()
            conn.execute_query(sqlcmd, (id, start_date, price))
            return redirect(url_for('product.index'))

    return render_template('product/update.html', product=product)


@bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
def delete(id):
    get_product(id)
    sqlcmd = """
    EXEC usp_DeleteProduct %s
    """
    conn = get_db()
    conn.execute_query(sqlcmd, id)
    return redirect(url_for('product.index'))
