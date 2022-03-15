from flask import Flask, jsonify
from read_from_data import main_read
import sqlite3

app = Flask(__name__)


@app.route('/<int:a_id>')
def main(a_id):
    data_read = main_read(a_id)

    return jsonify(data_read[0])
