from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return 'Are you lost?'


if __name__ == '__main__':
    app.run()