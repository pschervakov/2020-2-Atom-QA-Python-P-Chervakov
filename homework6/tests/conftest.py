import pytest
import settings
import requests
from socket_client import SocketClient
from http_mock_server import HTTPMockServer
from tests.http_mock_test_timeout import HTTPMockTimeoutServer
from tests.http_mock_test_500 import HTTPMock500Server
from my_app import run_app
from helpers import wait_until
import time
import requests


def shutdown_wait():
    requests.get(settings.APP_SHUTDOWN_URL)
    while True:
        try:
            requests.get(settings.APP_URL)
        except:
            break
            pass


@pytest.fixture(scope='session')
def run():
    mock = HTTPMockServer(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()
    run_app()
    yield
    mock.stop()
    shutdown_wait()



@pytest.fixture(scope='function')
def set_up(run):
    client = SocketClient(port=settings.APP_PORT, host=settings.APP_HOST)
    wait_until(client.connect)
    return client


@pytest.fixture(scope='function')
def set_up_mock_timeout():
    mock = HTTPMockTimeoutServer(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()
    wait_until(run_app)
    yield
    mock.stop()
    shutdown_wait()


@pytest.fixture(scope='function')
def set_up_mock_500():
    mock = HTTPMock500Server(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()
    run_app()
    yield
    requests.get(settings.MOCK_URL)
    mock.stop()
    shutdown_wait()


@pytest.fixture(scope='function')
def set_up_without_mock():
    run_app()
    yield
    shutdown_wait()
