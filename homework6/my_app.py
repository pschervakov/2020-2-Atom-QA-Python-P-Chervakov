import threading
import requests
from flask import Flask, request
import settings
from requests.exceptions import ConnectionError, Timeout

app = Flask(__name__)
DATA = []


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST,
        'port': settings.APP_PORT
    })

    server.start()
    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/list')
def list_sorts():
    return str(DATA), 200


def _new(sort):
    if sort in DATA:
        return "Sort already exists", 400
    else:
        DATA.append(sort)
        return f'Sort {sort} successfully added', 200


def _remove(sort):
    if sort in DATA:
        DATA.remove(sort)
        return f'Sort {sort} successfully removed', 200
    else:
        return "Sort doesn't exists", 400


def action(type_):
    if request.json is None:
        return 'Bad request', 400
    sort = request.json['sort']
    headers = request.headers
    try:
        mock_response = requests.get(url=f'{settings.MOCK_VALID_URL}', headers=headers, timeout=2)
    except ConnectionError:
        return 'Connection refused', 503
    except Timeout:
        return 'Server timed out', 503
    if mock_response.status_code == 500:
        return 'Server internal error', 503
    elif mock_response.status_code == 400:
        return 'Bad request'
    elif mock_response.status_code == 401:
        return "User doesn't exists", 401
    elif mock_response.status_code == 200:
        if type_ == 'setnew':
            return _new(sort)
        elif type_ == 'remove':
            return _remove(sort)


@app.route('/setnew', methods=['POST'])
def new():
    return action('setnew')


@app.route('/remove', methods=['POST'])
def remove():
    return action('remove')


if __name__ == '__main__':
    run_app()
