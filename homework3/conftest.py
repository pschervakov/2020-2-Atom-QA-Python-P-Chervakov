import pytest

from helpers import get_random_string
from my_target_client import MyTargetClient


@pytest.fixture(scope='function')
def api_config():
    user = 'kehimad482@teeshirtsprint.com'
    password = 'q12345'
    print('sth')
    client = MyTargetClient(user=user, password=password)
    return client


@pytest.fixture(scope='function')
def create_campaign(api_config):
    client = api_config
    name = get_random_string()
    client.create_segment(name)
    yield name
    client.delete_segment(name)
