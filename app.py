from flask import Flask, jsonify
from read_from_data import main_read

app = Flask(__name__)


@app.route('/<int:a_id>')
def main(a_id):
    """Возврат данных по животному"""
    data_read = main_read(a_id)

    return jsonify(data_read)
