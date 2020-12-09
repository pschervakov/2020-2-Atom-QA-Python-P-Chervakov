import socket
import json
import settings


def generate_request(method, url, headers, data=None):
    request = '{}\r\n{}\r\n\r\n{}'.format(
        method + ' ' + url + ' HTTP/1.1',
        '\r\n'.join(f'{key}: {value}' for key, value in headers.items()),
        data if data else '',
    )
    return request


class SocketClient:

    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.1)

    def connect(self):
        self.sock.connect((self.target_host, self.target_port))

    def collect_data(self):
        total_data = []
        while True:
            response = self.sock.recv(4096)
            if response:
                total_data.append(response.decode())

            else:
                break
        return ''.join(total_data).splitlines()

    def request(self, method, headers, url, data=None):
        request = generate_request(method=method, url=url, headers=headers, data=data)
        self.sock.send(request.encode())
        response = self.collect_data()
        return response
