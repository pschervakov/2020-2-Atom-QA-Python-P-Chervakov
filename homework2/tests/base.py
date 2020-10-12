import pytest

from pages.base_page import BasePage
from pages.campaign_page import CampaignPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.segment_page import SegmentPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.campaing_page = CampaignPage(driver)
        self.segment_page = SegmentPage(driver)
