import logging

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
