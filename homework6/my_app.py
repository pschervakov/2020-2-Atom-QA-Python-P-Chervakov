import threading
import requests
from urllib.parse import urljoin
from flask import Flask, request, jsonify
import settings

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


@app.route('/remove', methods=['POST'])
def remove():
    sort = request.json['sort']
    headers = request.headers
    mock_response = requests.get(url=f'{settings.MOCK_VALID_URL}', headers=headers)
    if mock_response.status_code == 400:
        return 'Bad request'
    elif mock_response.status_code == 401:
        return "User doesn't exists", 401
    elif mock_response.status_code == 200:
        if sort in DATA:
            DATA.remove(sort)
            return f'Sort {sort} successfully removed', 200
        else:
            return "Sort doesn't exists", 400


@app.route('/setnew', methods=['POST'])
def new():
    headers = request.headers
    if request.json is None:
        return 'Bad request', 400
    sort = request.json['sort']
    mock_response = requests.get(url=f'{settings.MOCK_VALID_URL}', headers=headers)
    if mock_response.status_code == 400:
        return 'Bad request'
    elif mock_response.status_code == 401:
        return "User doesn't exists", 401
    elif mock_response.status_code == 200:
        if sort in DATA:
            return "Sort already exists", 400
        else:
            DATA.append(sort)
            return f'Sort {sort} successfully added', 200


if __name__ == '__main__':
    run_app()
