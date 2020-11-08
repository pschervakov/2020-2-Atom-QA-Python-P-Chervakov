# import requests
# import settings
# import json
# from socket_client import SocketClient
# from http_mock_server import SimpleHTTPServer
# from my_app import run_app, shutdown_app
#
# host = "127.0.0.1"
# port = 1050
# client = SocketClient(host, port)
# client.connect()
#
# headers = {'Host': '127.0.0.1', 'User': 'Ivan'}
#
# resp = client.request(method='GET', headers=headers, url='/list')
# print(resp)
