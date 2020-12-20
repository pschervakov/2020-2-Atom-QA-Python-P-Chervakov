import threading
from flask import Flask, request
# from tests import settings


app = Flask(__name__)
data = ['philip']
MOCK_HOST = '0.0.0.0'
MOCK_PORT = '5050'


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
    })

    server.start()
    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


def is_user(username):
    return username in data


@app.route('/add_user/<username>')
def add_user(username):
    data.append(username)


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/vk_id/<username>')
def return_vk_id(username):
    if is_user(username):
        return {'vk_id': data.index(username)}, 200
    else:
        return {}, 404


if __name__ == '__main__':
    run_app()
