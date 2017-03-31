#  Copyright 2017
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   url_for,
                   jsonify)
from os import urandom
import requests

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


@app.route('/random_matrix_generation/create_matrix_database', methods=['PUT'])
def create_random_matrix_generation_database():
  try:
    requests_response = requests.put('http://random-matrix-generation'
                                     '/create_matrix_database')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'random-matrix-generation service: {}'
                   .format(e)}), 500


@app.route('/random_matrix_generation/create_matrix_tables', methods=['PUT'])
def create_random_matrix_generation_tables():
  try:
    requests_response = requests.put('http://random-matrix-generation'
                                     '/create_matrix_tables')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'random-matrix-generation service: {}'
                   .format(e)}), 500


@app.route('/random_matrix_generation/drop_matrix_database',
           methods=['DELETE'])
def drop_random_matrix_generation_database():
  try:
    requests_response = requests.delete('http://random-matrix-generation'
                                        '/drop_matrix_database')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'random-matrix-generation service: {}'
                   .format(e)}), 500


@app.route('/random_matrix_generation/drop_matrix_tables', methods=['DELETE'])
def drop_random_matrix_generation_tables():
  try:
    requests_response = requests.delete('http://random-matrix-generation'
                                        '/drop_matrix_tables')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'random-matrix-generation service: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/create_matrix_database', methods=['PUT'])
def create_matrix_multiplication_database():
  try:
    requests_response = requests.put('http://matrix-multiplication'
                                     '/create_matrix_database')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'matrix-multiplication service: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/create_matrix_tables', methods=['PUT'])
def create_matrix_multiplication_tables():
  try:
    requests_response = requests.put('http://matrix-multiplication'
                                     '/create_matrix_tables')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'matrix-multiplication service: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/drop_matrix_database', methods=['DELETE'])
def drop_matrix_multiplication_database():
  try:
    requests_response = requests.delete('http://matrix-multiplication'
                                        '/drop_matrix_database')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'matrix-multiplication service: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/drop_matrix_tables', methods=['DELETE'])
def drop_matrix_multiplication_tables():
  try:
    requests_response = requests.delete('http://matrix-multiplication'
                                        '/drop_matrix_tables')
    return (jsonify({'status': '{}'
                    .format(requests_response.json())}),
            requests_response.status_code)
  except Exception as e:
    return jsonify({'status': 'Error communicating with '
                    'matrix-multiplication service: {}'
                   .format(e)}), 500
