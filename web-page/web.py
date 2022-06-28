import asyncio
from asyncio import run

from flask import Flask, render_template

from scripts import secret_key, Database

app = Flask(__name__)

app.config['SECRET_KEY'] = asyncio.run(secret_key())

SQL = Database('../Products.db')


@app.route("/")
def index():
    return render_template('index.html', products = run(SQL.read_prod()), all_quantity_products = run(SQL.quantity_prod()), quantity_products = 10, Countdown_products = 1, page=1)

@app.route("/<page>")
def pages(page):
    try:
        page = int(page)
        all_quantity_products = run(SQL.quantity_prod())
        if (page < 0) or (page > all_quantity_products/10-1):
            return pageNotFount(404)
        return render_template('index.html', products = run(SQL.read_prod_more(page)), all_quantity_products = all_quantity_products, quantity_products = page*10+10, Countdown_products = page*10+1, page=page)
    except:
        return pageNotFount(404)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('features-404.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
