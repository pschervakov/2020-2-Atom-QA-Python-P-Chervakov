import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import settings


class MockHandleRequests(BaseHTTPRequestHandler):
    data = None
    valid_users = {'Ivan', 'Sergey'}

    def _set_headers(self, response=200):
        self.send_response(response)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/valid':
            headers = self.headers
            if 'User' not in headers:
                self._set_headers(400)
                self.wfile.write(b'BAD REQUEST')
            elif headers['User'] not in self.valid_users:
                self._set_headers(401)
                self.wfile.write(b'Access denied')
            else:
                self._set_headers(200)
                self.wfile.write(b'Hello')
        else:
            self._set_headers()
            self.wfile.write(b'Hello')

    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        response = self.rfile.read(content_length)
        self.wfile.write(b'Hello.\nThis is your data\n' + response)

    def do_PUT(self):
        self.do_POST()


class HTTPMockServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()


if __name__ == '__main__':
    mock = HTTPMockServer(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
    mock.start()

