import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import settings
from time import sleep

from http_mock_server import HTTPMockServer, MockHandleRequests


class Mock500HandleRequests(MockHandleRequests):
    def do_GET(self):
        self._set_headers(500)


class HTTPMock500Server(HTTPMockServer):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = Mock500HandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)


if __name__ == '__main__':
    mock = HTTPMock500Server(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()
    while True:
        pass
