import os
import json
from flask import Flask, render_template as render, flash, redirect, url_for, send_file

with open("/etc/cine.json") as config_file:
    config = json.load(config_file)

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = config['SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def home():

    return render('index.html')


@app.route('/category')
def category():

    return render('categoria.html')


@app.route('/selection')
def selection():

    return render('selection.html')


@app.route('/previous')
def previous():

    return render('previous.html')


@app.route('/ganadores')
def ganadores():

    return render('ganadores.html')


if __name__ == '__main__':
    #app.run(debug=True, host="172.16.170.129", port=8080)
    app.run(debug=True, host="localhost", port=8080)

