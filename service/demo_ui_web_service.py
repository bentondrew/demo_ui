#  Copyright 2017
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   redirect,
                   url_for)
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/demo_initialization', methods=['GET'])
def demo_initialization():
  return render_template('demo_initialization.html')


@app.route('/demo_execution', methods=['GET'])
def demo_execution():
  return render_template('demo_execution.html')
