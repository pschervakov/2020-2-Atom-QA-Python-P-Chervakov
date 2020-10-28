import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from helpers import get_random_string
from pages.login_page import LoginPage
from pages.main_page import MainPage


class AuthError(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--mail', default='kehimad482@teeshirtsprint.com')
    parser.addoption('--password', default='q12345')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope="function")
def driver(config):
    selenoid_server = config["selenoid"]
    if selenoid_server:
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': "chrome",
                        'version': '80',
                        }
        driver = webdriver.Remote(command_executor=f'http://{selenoid_server}/wd/hub/',
                                  desired_capabilities=capabilities
                                  )
    else:
        manager = ChromeDriverManager(version=config["version"])
        driver = webdriver.Chrome(executable_path=manager.install(),
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )
    driver.get(config['url'])
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def config(request: FixtureRequest):
    url = request.config.getoption('--url')
    mail = request.config.getoption('--mail')
    version = request.config.getoption('--browser_ver')
    password = request.config.getoption('--password')
    selenoid = request.config.getoption('--selenoid')
    lang = "en_US"
    return {"version": version, "url": url, "mail": mail, "password": password, "lang": lang, "selenoid": selenoid}


@pytest.fixture(scope="function")
def auth(driver, config):
    login_page = LoginPage(driver)
    page = login_page.login(config["mail"], config["password"])
    if driver.current_url == "https://target.my.com/dashboard":
        yield MainPage(driver)
    else:
        raise AuthError
    page.logout()


@pytest.fixture(scope="function")
def create_segment(driver, auth):
    name = get_random_string(10)
    main_page = auth
    segment_page = main_page.go_to_segments()
    segment_page.add_new_segment(name)
    yield segment_page, name
    segment_page.delete_segment(name)


@pytest.fixture(scope="function")
def create_campaign(driver, auth):
    name = get_random_string(5)
    main_page = auth
    campaign_page = main_page.go_to_campaigns()
    campaign_page.add_campaign(name)
    yield campaign_page, name
    campaign_page.delete_all_campaigns()
