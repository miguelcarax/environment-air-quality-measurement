#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)


@app.route('/')
def default():
    content = {'Hey men!': 'Are you lost?'}
    return content, status.HTTP_404_NOT_FOUND


@app.route('/air_quality', methods=['GET'])
def air_quality():
    """
    Return air quality measurements as a JSON
    """
    # FIXME: Return real data, no dummy ;(

    from models import AirQuality
    print(AirQuality.query.all())

    content = \
        {
            'TimeInstant': '2016-10-01 00:00:00.004',
            'id_entity': 'aq_salvia',
            'so2': 6.80117094260474,
            'no2': 48.398337879833704,
            'co': 0.657363926741451,
            'o3': 48.49706558445371,
            'pm10': 20.1015302324903,
            'pm2_5': 9.137353903174679
        }
    return content, status.HTTP_200_OK


if __name__ == '__main__':
    app.run()
