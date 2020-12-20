import requests
from tests.settings import APP_URl

from tests.settings import APP_URl, ADMIN_PASS,ADMIN_USER


class MyAppApClient:
    def __init__(self, user=ADMIN_USER, password=ADMIN_PASS):
        self.request_session = requests.Session()
        self.user = user
        self.password = password
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        self.cookies = None
        self.headers = None
        self.login()

    def login(self):
        url = f'{APP_URl}/login'
        data = {
            'username': self.user,
            'password': self.password,
            'submit': 'Login'
        }

        headers = {
            'User-Agent': self.user_agent
        }
        response = self.request_session.request('POST', url=f'{APP_URl}/login', headers=headers, json=data,
                                                allow_redirects=False)
        self.cookies = response.headers['set-cookie']
        self.headers = {
            'Cookie': self.cookies,
            'User-Agent': self.user_agent
        }

    def del_user(self, user):
        return requests.request('GET', url=f'{APP_URl}/api/del_user/{user}', headers=self.headers)

    def block_user(self, user):
        return requests.request('GET', url=f'{APP_URl}/api/block_user/{user}', headers=self.headers)

    def unblock_user(self, user):
        return requests.request('GET', url=f'{APP_URl}/api/accept_user/{user}', headers=self.headers)

    def add_user(self, name, password, email):
        data = {
            "username": name,
            "password": password,
            "email": email
        }
        return requests.request('POST', url=f'{APP_URl}/api/add_user', headers=self.headers, json=data)

    def check_status(self):
        return requests.request('GET', url=f'{APP_URl}/status', headers=self.headers)
