#  Copyright 2017
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   url_for,
                   jsonify)
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


@app.route('/random_matrix_generation/create_matrix_database', methods=['PUT'])
def create_random_matrix_generation_database():
  try:
    #  TODO: Send request to random-matrix-generation service
    return jsonify({'status': 'Successfully created matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix database: {}'
                   .format(e)}), 500


@app.route('/random_matrix_generation/create_matrix_tables', methods=['PUT'])
def create_random_matrix_generation_tables():
  try:
    #  TODO: Send request to random-matrix-generation service
    return jsonify({'status': 'Successfully created matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix tables: {}'
                   .format(e)}), 500


@app.route('/random_matrix_generation/drop_matrix_database',
           methods=['DELETE'])
def drop_random_matrix_generation_database():
  try:
    #  TODO: Send request to random-matrix-generation service
    return jsonify({'status': 'Successfully dropped matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix database: {}'
                   .format(e)}), 500


@app.route('/random_matrix_generation/drop_matrix_tables', methods=['DELETE'])
def drop_random_matrix_generation_tables():
  try:
    #  TODO: Send request to random-matrix-generation service
    return jsonify({'status': 'Successfully dropped matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix tables: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/create_matrix_database', methods=['PUT'])
def create_matrix_multiplication_database():
  try:
    #  TODO: Send request to matrix-multiplication service
    return jsonify({'status': 'Successfully created matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix database: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/create_matrix_tables', methods=['PUT'])
def create_matrix_multiplication_tables():
  try:
    #  TODO: Send request to matrix-multiplication service
    return jsonify({'status': 'Successfully created matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix tables: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/drop_matrix_database', methods=['DELETE'])
def drop_matrix_multiplication_database():
  try:
    #  TODO: Send request to matrix-multiplication service
    return jsonify({'status': 'Successfully dropped matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix database: {}'
                   .format(e)}), 500


@app.route('/matrix_multiplication/drop_matrix_tables', methods=['DELETE'])
def drop_matrix_multiplication_tables():
  try:
    #  TODO: Send request to matrix-multiplication service
    return jsonify({'status': 'Successfully dropped matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix tables: {}'
                   .format(e)}), 500
