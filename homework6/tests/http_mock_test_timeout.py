import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import settings
from time import sleep

from http_mock_server import HTTPMockServer, MockHandleRequests


class TimeoutMockHandleRequests(MockHandleRequests):
    def do_GET(self):
        sleep(3)


class HTTPMockTimeoutServer(HTTPMockServer):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = TimeoutMockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)


if __name__ == '__main__':
    mock = HTTPMockTimeoutServer(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()
    while True:
        pass
