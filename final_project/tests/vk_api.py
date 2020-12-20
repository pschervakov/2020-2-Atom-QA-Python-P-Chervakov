import requests

MOCK_PORT, MOCK_HOST = '5050', 'vk'


class VKApiClient:
    url = f'http://{MOCK_HOST}:{MOCK_PORT}'

    def add_user(self, name):
        requests.get(f'{self.url}/add_user/{name}')

    def get_id(self, name):
        return requests.get(f'{self.url}/vk_id/{name}')
