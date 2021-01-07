#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis
import requests
import sys
from flask import Flask
from flask_api import status

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

################################################################################
# Redis Configuration
################################################################################
redis_client = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT
    # No password by default
    # password=Config.REDIS_PASSWORD
)

# Check redis connection
try:
    redis_client.ping()

except redis.ConnectionError:
    print('It\'s not possible to connect to Redis')
    sys.exit(1)


# Unique entry point for all calls
@app.route('/', methods=['GET'])
@app.route('/<path:text>', methods=['GET'])
def default(text=''):
    """
    Check if there is a cached response for that route.
        If it's a cache hit it serves the content from the cache
        If it's a cache miss it redirects the call to the backend, return the content and
            update the cache

    @text -> The path in the HTTP Request

    TODO:
        + The app should update the cache asynchronously to avoid delay
        + Log if there is a cache miss or miss hit
    """
    request_hash = str(hash(text))

    # Cache hit
    if redis_client.exists(request_hash):
        content = redis_client.get(request_hash)
        response_code = status.HTTP_200_OK

    # Cache miss
    else:
        backend_response = requests.get('http://{}:{}/{}'.format(
            Config.BACKEND_HOST,
            Config.BACKEND_PORT,
            text
        ))
        content = backend_response.content
        response_code = backend_response.status_code
        # Update cache
        # Set expiration time to 30 seconds
        redis_client.set(
            name=request_hash,
            value=content,
            ex=30
        )

    return content, response_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
