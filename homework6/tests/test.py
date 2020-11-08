import pytest
import json
import settings
from socket_client import SocketClient
from my_app import DATA


class TestApp:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, my_client):
        self.client = my_client

    def get_items(self, response):
        str_ = response[-1][1:-1].replace(' ', '')
        lst = str_.split(',')
        return lst

    def test_setnew(self, run):
        data = {'sort': 'Apple'}
        data = json.dumps(data)
        headers = {'Host': '127.0.0.1', 'User': 'Ivan', 'Content-Type': 'application/json',
                   'Content-length': len(data.encode())}
        response = self.client.request(method='POST', headers=headers, url='/setnew', data=data)
        assert response[-1] == 'Sort Apple successfully added'

    def test_setnew_negative(self):
        DATA.append('Apple')
        data = {'sort': 'Apple'}
        data = json.dumps(data)
        headers = {'Host': '127.0.0.1', 'User': 'Ivan', 'Content-Type': 'application/json',
                   'Content-length': len(data.encode())}
        response = self.client.request(method='POST', headers=headers, url='/setnew', data=data)
        assert response[-1] == 'Sort already exists'

    def test_remove_positive(self, run):
        DATA.append('Orange')
        data = {'sort': 'Orange'}
        data = json.dumps(data)
        headers = {'Host': '127.0.0.1', 'User': 'Ivan', 'Content-Type': 'application/json',
                   'Content-length': len(data.encode())}
        response = self.client.request(method='POST', headers=headers, url='/remove', data=data)
        assert response[-1] == 'Sort Orange successfully removed'

    def test_remove_negative(self, run):
        data = {'sort': 'Orange'}
        data = json.dumps(data)
        headers = {'Host': '127.0.0.1', 'User': 'Ivan', 'Content-Type': 'application/json',
                   'Content-length': len(data.encode())}
        response = self.client.request(method='POST', headers=headers, url='/remove', data=data)
        assert response[-1] == "Sort doesn't exists"

    def test_list(self):
        DATA.append('Multifruit')
        headers = {'Host': '127.0.0.1', 'User': 'Ivan'}
        response = self.client.request(method='GET', headers=headers, url='/list')
        lst = self.get_items(response)
        assert "'Multifruit'" in lst
