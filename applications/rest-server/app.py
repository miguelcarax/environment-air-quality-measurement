from flask import Flask
from flask_api import status

app = Flask(__name__)


@app.route('/')
def default():
    content = {'Hey men!': 'Are you lost?'}
    return content, status.HTTP_404_NOT_FOUND


if __name__ == '__main__':
    app.run()
