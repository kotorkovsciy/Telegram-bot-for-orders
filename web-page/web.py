import asyncio

from flask import Flask, render_template

from scripts import secret_key

app = Flask(__name__)

app.config['SECRET_KEY'] = asyncio.run(secret_key())


@app.route("/")
def index():
    return render_template('index.html')

@app.errorhandler(404)
def pageNotFount(error):
    return render_template('features-404.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)