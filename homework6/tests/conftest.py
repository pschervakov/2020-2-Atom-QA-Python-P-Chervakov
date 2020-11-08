import pytest
import flask
import settings
import requests
from socket_client import SocketClient
from http_mock_server import SimpleHTTPServer
from my_app import run_app, shutdown_app
import time


@pytest.fixture(scope='session')
def run():
    mock = SimpleHTTPServer(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()
    run_app()
    time.sleep(2)
    yield
    requests.get(settings.APP_SHUTDOWN_URL)
    requests.get(settings.MOCK_SHUTDOWN_URL)
    # shutdown_app()
    # mock.stop()


@pytest.fixture(scope='function')
def my_client():
    client = SocketClient(port=settings.APP_PORT, host=settings.APP_HOST)
    client.connect()
    return client
