import pytest

from helpers import get_random_string

@pytest.mark.API
class Test():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_config):
        self.client = api_config

    def test_create_segment(self, create_campaign):
        name = create_campaign
        names = self.client.segments_list()
        assert name in names

    def test_delete_segment(self):
        name = get_random_string(5)
        self.client.create_segment(name)
        self.client.delete_segment(name)
        names = self.client.segments_list()
        assert name not in names
