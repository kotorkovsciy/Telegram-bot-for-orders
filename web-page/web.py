import asyncio
from asyncio import run

from flask import Flask, render_template

from scripts import secret_key, Database

app = Flask(__name__)

app.config['SECRET_KEY'] = asyncio.run(secret_key())

SQL = Database('../Products.db')


@app.route("/")
def index():
    return render_template('index.html', products = run(SQL.read_prod()), quantity_products = run(SQL.quantity_prod()))


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('features-404.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
