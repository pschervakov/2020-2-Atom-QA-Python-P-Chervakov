import pytest
from tests.ui.pages.base_page import BasePage
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.reg_page import RegPage
from tests.ui.pages.main_page import MainPage, expected_titles
from tests.vk_api import VKApiClient
from tests.helpers import get_data, get_incorrect_email, get_incorrect_name, get_correct_name
from tests import settings
from tests.myapp_api import MyAppApClient
import allure


@pytest.mark.usefixtures("screenshot_on_failure")
@allure.feature('UI tests')
class TestUI:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, builder, vk_client, api_client):
        self.api_client = api_client
        self.vk_api = vk_client
        self.sql_builder = builder
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.reg_page = RegPage(driver)
        self.main_page = MainPage(driver)


@allure.story('login')
class TestLogin(TestUI):

    def test_login(self):
        """Correct login"""
        name, password = settings.ADMIN_USER, settings.ADMIN_PASS
        with allure.step('login'):
            self.login_page.login(user=name, password=password)
        with allure.step('check correct page and username'):
            assert f'Logged as {settings.ADMIN_USER}' in self.driver.page_source
        with allure.step('check database'):
            assert self.sql_builder.get_record_by_name(name).active == 1

    def test_incorrect_login(self):
        """Incorrect login """
        name, _, password = get_data()
        with allure.step('login'):
            self.login_page.login(user=name, password=password)
        with allure.step('check correct response'):
            assert 'Invalid username or password'
        with allure.step('check database'):
            assert self.sql_builder.get_record_by_name(name) == -1

    def test_login_blocked_user(self, data, block):
        """Login with blocked user"""
        name, _, password = data
        with allure.step('login as blocked user'):
            self.login_page.login(user=name, password=password)
        with allure.step('check correct response'):
            assert 'Ваша учетная запись заблокирована' in self.driver.page_source


@allure.story('registration')
@pytest.mark.usefixtures("go_to_reg_page")
class TestRegistration(TestUI):
    def test_correct_reg(self, del_user, data):
        """Correct registration """
        name, email, password = data
        with allure.step('reg user'):
            self.reg_page.reg(user=name, password=password, email=email)
        with allure.step('check correct page and username'):
            assert f'Logged as {name}' in self.driver.page_source

    @pytest.mark.xfail(reason='field "active" is incorrect')
    def test_correct_reg_db(self, del_user, data):
        """Correct registration (db fields)"""
        name, email, password = data
        with allure.step('reg user'):
            self.reg_page.reg(user=name, password=password, email=email)
        record = self.sql_builder.get_record_by_name(name)
        with allure.step('check correct username in db'):
            assert record.username == name
        with allure.step('check correct password in db'):
            assert record.password == password
        with allure.step('check correct email in db'):
            assert record.email == email
        with allure.step('check correct access in db'):
            assert record.access == 1
        with allure.step('check correct active in db'):
            assert record.active == 1

    def test_incorrect_username_length(self):
        """Incorrect username length"""
        user, email, password = get_data(name=get_incorrect_name)
        with allure.step('reg user'):
            self.reg_page.reg(user=user, password=password, email=email)
        with allure.step('check correct response'):
            assert "Incorrect username length" in self.driver.page_source

    def test_incorrect_email(self):
        """Incorrect user email"""
        user, email, password = get_data(email=get_incorrect_email)
        with allure.step('reg user'):
            self.reg_page.reg(user=user, password=password, email=email)
        with allure.step('check correct response'):
            assert "Invalid email address" in self.driver.page_source

    @pytest.mark.xfail(reason='adding a user with existing email causes internal error')
    def test_duplicate_email(self, add_del, data):
        """Adding a user with existing email"""
        user, email, password = data
        user2 = get_correct_name()
        with allure.step('reg user'):
            self.reg_page.reg(user=user2, password=password, email=email)
        with allure.step('Check that invalid user does not exists'):
            assert self.sql_builder.get_record_by_name(user2) == -1
        with allure.step('check correct response'):
            assert "Internal Server Error" not in self.driver.page_source

    def test_diff_passwords(self):
        """Password fields don't match"""
        user, email, password = get_data()
        with allure.step('reg user'):
            self.reg_page.reg(user=user, password=password, rpassword=password + '1', email=email)
        with allure.step('check correct response'):
            assert "Passwords must match" in self.driver.page_source

    @pytest.mark.xfail(reason='when two wrong fields passed app response is incorrect ')
    def test_two_wrong_fields(self):
        """Two fields are incorrect"""
        user, email, password = get_data(name=get_incorrect_name)
        with allure.step('reg user'):
            self.reg_page.reg(user=user, password=password, rpassword=password + '1', email=email)
        with allure.step('check correct response'):
            assert "{'username': ['Incorrect username length'], 'password': ['Passwords must match']}" not in self.driver.page_source

    @pytest.mark.xfail(reason='when two empty fields passed app response is incorrect ')
    def test_two_empty_fields(self):
        user, _, password = get_data()
        with allure.step('reg user'):
            self.reg_page.reg(user=user, password=password, rpassword='', email='')
        with allure.step('check correct response'):
            assert "{'email': ['Incorrect email length', 'Invalid email address'], 'password': ['Passwords must match']}" not in self.driver.page_source

    @pytest.mark.xfail(reason='the app does not trim spaces in the username')
    def test_spaces_in_name(self, data, name_with_spaces):
        """Username with spaces"""
        name, email, password = data
        name_with_space = name_with_spaces
        with allure.step('reg user'):
            self.reg_page.reg(user=name_with_space, password=password, email=email)
        with allure.step('Check that name with spaces does not exists'):
            assert self.sql_builder.get_record_by_name(name) != -1

    @pytest.mark.xfail(reason='the app does not trim spaces in the password')
    def test_spaces_in_password(self, data):
        """Spaces in password"""
        name, email, password = data
        pass_with_space = ' ' * 3 + password
        with allure.step('reg user'):
            self.reg_page.reg(user=name, password=pass_with_space, email=email)
        with allure.step('check that password is saved without a space'):
            assert self.sql_builder.get_record_by_name(name).password == password


@allure.story('main page')
class TestMainPage(TestUI):
    @pytest.mark.parametrize('locator,expect_title', expected_titles)
    def test_links(self, login, locator, expect_title):
        """Check page links"""
        with allure.step('go to link'):
            self.main_page.go_to(locator)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        with allure.step('Check link'):
            assert self.main_page.check_title(expect_title)

    @pytest.mark.xfail(reason='link at "Centos" is incorrect')
    def test_centos(self, login):
        """Check centos link"""
        with allure.step('go to link'):
            self.main_page.go_to('centos')
        with allure.step('Check link'):
            assert self.main_page.check_title('Centos7')

    def test_logout(self, data, del_user, go_to_reg_page):
        """Logout"""
        name, email, password = data
        self.reg_page.reg(user=name, password=password, email=email)
        self.main_page.logout()
        with allure.step('check correct page'):
            assert self.login_page.is_instance()
        with allure.step('check correct active field '):
            assert self.sql_builder.get_record_by_name(name).active == 0

    def test_vk_id(self, data, go_to_reg_page):
        """Check that vk id appears"""
        name, email, password = data
        with allure.step('add user to vk'):
            self.vk_api.add_user(name)
        with allure.step('reg user'):
            self.reg_page.reg(user=name, password=password, email=email)
        with allure.step('check that vk id appears'):
            assert 'VK ID: 1' in self.driver.page_source

    @pytest.mark.xfail(reason='vk id:0 does not appear')
    def test_vk_id_fail(self, login):
        """Check that vk id appears"""
        with allure.step('check that vk id appears'):
            assert 'VK ID: 0' in self.driver.page_source

    @pytest.mark.xfail(reason='field "active" is not set to zero after blocking')
    def test_block_active(self, del_user, data):
        """Check that blocked user is not active"""
        name, email, password = data
        with allure.step('add new user and login'):
            self.sql_builder.add_user(name=name, email=email, password=password)
            self.login_page.login(user=name, password=password)
        with allure.step('block user'):
            self.api_client.block_user(name)
        with allure.step('check correct active field'):
            assert self.sql_builder.get_record_by_name(name).active == 0

    def test_block(self, del_user, data, go_to_reg_page):
        """Check that blocked user redirects on login page"""
        name, email, password = data
        with allure.step('reg new user and block'):
            self.reg_page.reg(user=name, password=password, email=email)
            self.api_client.block_user(name)
        with allure.step('check that user has no access'):
            self.driver.get(f'{settings.APP_URl}/welcome')
            assert "This page is available only to authorized users" in self.driver.page_source
