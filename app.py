from flask import Flask, jsonify, abort
from flask_cors import CORS

import database
from process_covid import process_covid
from load_data import load

app = Flask(__name__)
cors = CORS(app)


@app.route('/load', methods=['POST'])
def load_data():
    load()
    return 'ok'


@app.route('/series/process', methods=['POST'])
def execute_process_covid():
    process_covid()
    return 'ok'


@app.route('/series/country/<country_code>', methods=['GET'])
def get_series_by_country_code(country_code):
    series = database.get_series_by_code(country_code)
    if series:
        for s in series:
            del s['_id']
        return jsonify(series)
    return abort(404)


@app.route('/country/<country_code>', methods=['GET'])
def get_country(country_code):
    country = database.get_country(country_code)
    if country:
        del country['_id']
        return jsonify(country)
    return abort(404)


if __name__ == '__main__':
    app.run()
