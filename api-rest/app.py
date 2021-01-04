#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep

from flask import Flask, jsonify
from flask_api import status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from models import AirQuality

app = Flask(__name__)
app.config.from_object(Config)

# Added some delay to let Postgres initialize some data
sleep(1)
engine = create_engine(Config.DATABASE_URI)
# Define Session Factory for incoming requests
Session = sessionmaker(bind=engine)


@app.route('/')
def default():
    """
    Default route for testing purpose
    """
    content = {'Hey men!': 'Are you lost?'}
    return content, status.HTTP_404_NOT_FOUND


@app.route('/air_quality', methods=['GET'])
def air_quality():
    """
    Return ALL air quality measurements as a JSON
    """
    session = Session()
    measurements = session.query(AirQuality).all()
    session.close()

    return jsonify([measurement.to_dict() for measurement in measurements]), status.HTTP_200_OK


if __name__ == '__main__':
    app.run(host='0.0.0.0')
