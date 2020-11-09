import json


class BaseTest:
    def setnew(self, client, data, headers):
        return client.request(method='POST', headers=headers, url='/setnew', data=data)

    def remove(self, client, data, headers):
        return client.request(method='POST', headers=headers, url='/remove', data=data)

    def list(self, client, headers):
        return client.request(method='GET', headers=headers, url='/list')

    def get_headers(self, length=None, user='Ivan'):
        if user is None:
            return {'Host': '127.0.0.1', 'Content-Type': 'application/json',
                    'Content-length': length}
        elif length is None:
            return {'Host': '127.0.0.1', 'User': user}
        else:
            return {'Host': '127.0.0.1', 'User': user, 'Content-Type': 'application/json',
                    'Content-length': length}

    def get_items(self, response):
        str_ = response[-1][1:-1].replace(' ', '')
        lst = str_.split(',')
        return lst

    def get_info(self, user='Ivan', sort=None):
        data = None
        if sort:
            data = {'sort': sort}
            data = json.dumps(data)
        headers = self.get_headers(length=(len(data.encode())), user=user)
        return data, headers
