import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class NoSuchSegmentException(Exception):
    pass


class MyTargetClient:
    def __init__(self, user, password):
        self.session = requests.Session()
        self.csrf_token = None
        self.user = user
        self.password = password
        self.login()

    def _request(self, method, url, status_code=200, headers=None, params=None, data=None, json=True,
                 allow_redirects=True, json_data=None):
        response = self.session.request(method, url, headers=headers, params=params, data=data,
                                        allow_redirects=allow_redirects, json=json_data)
        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        if json:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" failed with error "{error}"!')
            return json_response
        return response

    def login(self):
        url = 'https://auth-ac.my.com/auth'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'

        }
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/',
        }
        params = {'lang': 'ru', 'nosavelogin': '0'}
        response = self._request('POST', url, params=params, headers=headers, data=data, json=False)
        response = self._request('GET', 'https://target.my.com/csrf/', json=False)
        self.csrf_token = response.headers['set-cookie'].split(';')[0].split('=')[1]

    def create_segment(self, name):
        headers = {
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.csrf_token,
        }
        url = 'https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        data = {'name': name, 'pass_condition': 1, 'logicType': 'or',
                'relations': [
                    {'object_type': 'remarketing_player', 'params': {'type': 'positive', 'left': 365, 'right': 0}}],
                }
        self._request('POST', url, json=False, json_data=data, headers=headers)

    def segments_list(self):
        url = 'https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags&limit=500&_=160287138171'
        response = self._request('GET', url)
        seg_names = []
        for el in response['items']:
            seg_names.append(el['name'])
        return seg_names

    def delete_segment(self, name):
        url = 'https://target.my.com/api/v1/remarketing/mass_action/delete.json'
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token,
        }
        seg_id = self.get_segment_id_by_name(name)
        data = [{'source_id': seg_id, 'source_type': 'segment'}]
        self._request('POST', json_data=data, headers=headers, url=url)

    def get_segment_id_by_name(self, name):
        url = 'https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags&limit=500&_=160287138171'
        response = self._request('GET', url)
        seg_id = None
        for el in response['items']:
            if el['name'] == name:
                seg_id = el['id']
        if seg_id:
            return seg_id
        else:
            raise NoSuchSegmentException
