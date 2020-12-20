import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests import settings
from tests.ui.fixtures import *
import allure
import time

def pytest_addoption(parser):
    parser.addoption('--url', default=settings.APP_URl)
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default='selenoid:4444')


@pytest.fixture(scope="function")
def driver(config):
    selenoid_server = config["selenoid"]
    if selenoid_server:
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("start-maximized")
        # chrome_options.add_argument('disable-infobars')
        # chrome_options.add_argument('--disable-web-security')
        # new_capabilities = chrome_options.to_capabilities()
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': "chrome",
                        'version': '80',
                        }
        # capabilities.update(new_capabilities)

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
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')

    return {"version": version, "url": url, "selenoid": selenoid}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        time.sleep(1)
        allure.attach(body=driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
