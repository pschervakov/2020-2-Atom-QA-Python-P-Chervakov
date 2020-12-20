from tests.myapp_api import MyAppApClient
import allure
import pytest
from requests import request
from tests.settings import APP_URl
from tests.helpers import get_random_string, get_correct_email, get_data, get_incorrect_name, get_incorrect_email, \
    get_correct_name


@allure.feature('API tests')
class TestApi:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, connection, builder,api_client):
        self.client = api_client
        self.sql_connection = connection
        self.sql_builder = builder

    @allure.story('add user')
    @pytest.mark.xfail(reason='wrong status code')
    def test_add_user(self, data, del_user):
        """Adding a user"""
        name, email, password = data
        with allure.step('adhttps://github.com/snicks92/technoatom-qa-pythond user'):
            response = self.client.add_user(name=name, password=password, email=email)
        with allure.step('Check that the user in the db'):
            assert name in self.sql_builder.get_usernames()
        with allure.step('Check status code'):
            assert response.status_code == 201

    @allure.story('add user')
    def test_add_user_exists(self, data, del_user):
        """Adding an existing user"""
        name, email, password = data
        with allure.step('add two identical users'):
            self.sql_builder.add_user(name=name, password=password, email=email)
            response = self.client.add_user(name=name, password=password, email=email)
        with allure.step('Check status code'):
            assert response.status_code == 304

    @allure.story('add user')
    @pytest.mark.xfail(reason='field "username" does not validate')
    def test_add_user_incorrect(self, incorrect_name):
        """Adding user with incorrect username"""
        name, email, password = incorrect_name
        with allure.step('add user'):
            response = self.client.add_user(name=name, email=email, password=password)
        with allure.step('Check that invalid user does not exists'):
            assert self.sql_builder.get_record_by_name(name) == -1
        with allure.step('Check status code'):
            assert response.status_code == 400

    @allure.story('add user')
    @pytest.mark.xfail(reason='field "email" does not validate')
    def test_add_email_incorrect(self, data, del_user):
        """Adding a user with an incorrect email"""
        name, _, password = data
        email = get_incorrect_email()
        with allure.step('add user'):
            response = self.client.add_user(name=name, email=email, password=password)
        with allure.step('Check that invalid user does not exists'):
            assert self.sql_builder.get_record_by_name(name) == -1
        with allure.step('Check status code'):
            assert response.status_code == 400

    @allure.story('add user')
    @pytest.mark.xfail(reason='incorrect status code')
    def test_add_duplicate_email(self, data, add_del):
        """Adding  a user with an existing email"""
        name, email, password = data
        name2 = get_correct_name()
        with allure.step('add user'):
            response = self.client.add_user(name=name2, password=password, email=email)
        with allure.step('Check status code'):
            assert response.status_code == 304

    @allure.story('add user')
    @pytest.mark.xfail(reason='api allow empty password')
    def test_add_user_empty_password(self, data, add_del):
        """Adding  a user with an empty password"""
        name, email, _ = data
        with allure.step('add user'):
            response = self.client.add_user(name=name, password=' ', email=email)
        with allure.step('Check that invalid user does not exists'):
            assert self.sql_builder.get_record_by_name(name) == -1
        with allure.step('Check status code'):
            assert response.status_code == 400

    @allure.story('delete user')
    def test_del_user(self, data, add_user):
        """Deleting a user"""
        name, email, password = data
        with allure.step('delete user'):
            response = self.client.del_user(name)
        with allure.step('Check that deleted user not in the db'):
            assert name not in self.sql_builder.get_usernames()
        with allure.step('Check status code'):
            assert response.status_code == 204

    @allure.story('delete user')
    def test_del_user_exists(self):
        """Deleting an existing user"""
        name, email, password = get_data()
        with allure.step('delete existing user'):
            response = self.client.del_user(user=name)
        with allure.step('Check status code'):
            assert response.status_code == 404

    @allure.story('status')
    def test_status(self):
        """App status"""
        with allure.step('Check status code'):
            assert self.client.check_status().status_code == 200

    @allure.story('block user')
    def test_block(self, data, add_del):
        """Block a user"""
        name, email, password = data
        with allure.step('block user'):
            response = self.client.block_user(name)
        record = self.sql_builder.get_record_by_name(name)
        with allure.step('Check that access changed'):
            assert record.access == 0
        with allure.step('Check status code'):
            assert response.status_code == 200

    @allure.story('block user')
    def test_block_blocked(self, data, block):
        """Block a user that already blocked"""
        name, email, password = data
        with allure.step('block user'):
            response = self.client.block_user(name)
        with allure.step('Check status code'):
            assert response.status_code == 304

    @allure.story('unblock user')
    def test_unblock(self, data, block):
        """Unblock a user"""
        name, email, password = data
        with allure.step('unblock user'):
            response = self.client.unblock_user(name)
        record = self.sql_builder.get_record_by_name(name)
        with allure.step('Check that access changed'):
            assert record.access == 1
        with allure.step('Check status code'):
            assert response.status_code == 200

    @allure.story('unblock user')
    def test_unblock_unblocked(self, data, add_del):
        """Unblock a user that already unblocked"""
        name, email, password = data
        with allure.step('unblock user'):
            response = self.client.unblock_user(name)
        with allure.step('Check status code'):
            assert response.status_code == 304

    @allure.story('unauthorized')
    def test_unauthorized(self):
        """Unauthorized request"""
        with allure.step('try unauthorized request'):
            response = request('GET', url=f'{APP_URl}/api/del_user/random')
        with allure.step('Check status code'):
            assert response.status_code == 401

    @allure.story('login')
    @pytest.mark.xfail(reason='incorrect status code')
    def test_incorrect_login(self, data):
        """Incorrect login request """
        with allure.step('try incorrect request at login'):
            response = request('POST', url=f'{APP_URl}/login')
        with allure.step('Check status code'):
            assert response.status_code != 200

    @allure.story('bad request')
    def test_bad_request(self):
        with allure.step('try bad request'):
            response = request('POST', url=f'{APP_URl}/api/add_user')
        with allure.step('Check status code'):
            assert response.status_code == 401
