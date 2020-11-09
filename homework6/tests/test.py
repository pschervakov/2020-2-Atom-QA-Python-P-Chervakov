import json
from time import sleep

import pytest
from helpers import wait_until
import settings
from socket_client import SocketClient
from tests.base_test import BaseTest
from my_app import DATA


#@pytest.mark.skip
class TestApp(BaseTest):
    def test_mock_unavailable(self, set_up_without_mock):
        client = SocketClient(port=settings.APP_PORT, host=settings.APP_HOST)
        wait_until(client.connect)
        data = {'sort': 'Apple'}
        data = json.dumps(data)
        headers = self.get_headers(len(data.encode()))
        response = client.request(method='POST', headers=headers, url='/setnew', data=data)
        assert response[-1] == 'Connection refused'

    def test_mock_500(self, set_up_mock_500):
        client = SocketClient(port=settings.APP_PORT, host=settings.APP_HOST)
        wait_until(client.connect)
        data, headers = self.get_info(sort='Apple')
        response = client.request(method='POST', headers=headers, url='/setnew', data=data)
        assert response[-1] == 'Server internal error'

    def test_mock_timeout(self, set_up_mock_timeout):
        client = SocketClient(port=settings.APP_PORT, host=settings.APP_HOST)
        wait_until(client.connect)
        client.sock.settimeout(3.1)
        data, headers = self.get_info(sort='Apple')
        response = client.request(method='POST', headers=headers, url='/setnew', data=data)
        assert response[-1] == 'Server timed out'

# @pytest.mark.skip
class TestAppNormal(BaseTest):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, set_up):
        self.client = set_up

    def test_setnew(self):
        data, headers = self.get_info(sort='Apple')
        response = self.setnew(client=self.client, headers=headers, data=data)
        assert response[-1] == 'Sort Apple successfully added'

    def test_setnew_negative(self):
        DATA.append('Apple')
        data, headers = self.get_info(sort='Apple')
        response = self.setnew(client=self.client, headers=headers, data=data)
        assert response[-1] == 'Sort already exists'

    def test_remove_positive(self):
        DATA.append('Orange')
        data, headers = self.get_info(sort='Orange')
        response = self.remove(client=self.client, headers=headers, data=data)
        assert response[-1] == 'Sort Orange successfully removed'

    def test_remove_negative(self):
        data, headers = self.get_info(sort='Orange')
        response = self.remove(client=self.client, headers=headers, data=data)
        assert response[-1] == "Sort doesn't exists"

    def test_list(self):
        DATA.append('Multifruit')
        headers = self.get_headers()
        response = self.list(client=self.client, headers=headers)
        lst = self.get_items(response)
        assert "'Multifruit'" in lst

    def test_mock_headerless(self):
        data, headers = self.get_info(sort='Apple', user=None)
        response = self.setnew(client=self.client, headers=headers, data=data)
        assert response[-1] == 'Bad request'

    def test_mock_header_invalid(self):
        data, headers = self.get_info(sort='Apple', user='Kirill')
        response = self.remove(client=self.client, headers=headers, data=data)
        assert response[-1] == "User doesn't exists"
