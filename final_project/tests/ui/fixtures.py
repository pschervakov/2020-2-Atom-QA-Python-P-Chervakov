import pytest
from tests.ui.pages.reg_page import RegPage
from tests.ui.pages.login_page import LoginPage
from tests.my_sql_client import MySqlConnection
from tests.mysql_builder import MySqlBuilder
from tests.helpers import get_data, get_incorrect_name
from tests import settings
from tests.myapp_api import MyAppApClient
from tests.vk_api import VKApiClient

@pytest.fixture(scope='function')
def reg_page(driver):
    return RegPage(driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def go_to_reg_page(login_page):
    login_page.go_to_reg_page()

@pytest.fixture(scope='function')
def connection():
    return MySqlConnection()


@pytest.fixture(scope='function')
def builder(connection):
    return MySqlBuilder(connection)

@pytest.fixture(scope='function')
def api_client():
    return MyAppApClient()
@pytest.fixture(scope='function')
def vk_client():
    return VKApiClient()

@pytest.fixture(scope='function')
def login(login_page):
    login_page.login()


@pytest.fixture(scope='function')
def data():
    return get_data()


@pytest.fixture(scope='function')
def name_with_spaces(data, builder):
    name = data[0]
    name_with_spaces = ' ' * 3 + name
    yield name_with_spaces
    builder.delete_user(name_with_spaces)


@pytest.fixture(scope='function')
def incorrect_name(data, builder):
    _, email, password = data
    name = get_incorrect_name()
    yield name, email, password
    builder.delete_user(name)




@pytest.fixture(scope='function')
def add_user(builder, data):
    user, email, password = data
    builder.add_user(name=user, email=email, password=password)


@pytest.fixture(scope='function')
def del_user(builder, data):
    yield
    user, email, password = data
    builder.delete_user(name=user)


@pytest.fixture(scope='function')
def add_del(builder, data):
    user, email, password = data
    builder.add_user(name=user, email=email, password=password)
    yield
    builder.delete_user(name=user)


@pytest.fixture(scope='function')
def block(add_del, builder, data):
    user, email, password = data
    builder.block_user(user)


@pytest.fixture(scope='function')
def unblock_admin(builder):
    builder.unblock_user(settings.ADMIN_USER)
