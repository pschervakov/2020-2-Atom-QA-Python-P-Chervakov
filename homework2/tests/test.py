import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
from helpers import get_random_string
from tests.base import BaseCase


@pytest.mark.UI
class Test(BaseCase):
    def test_auth(self):
        mail = self.config['mail']
        password = self.config['password']
        self.login_page.login(mail, password)
        assert self.base_page.find(self.base_page.locators.PROFILE_NAME)

    def test_auth_negative(self):
        mail = "incorrectmail@mail.ru"
        password = "incorrectpassword"
        str = "Invalid login or password"
        self.login_page.login(mail, password)
        self.base_page.wait().until(lambda d: str in d.page_source)
        assert str in self.driver.page_source

    def test_create_segment(self, create_segment):
        segment_page, name = create_segment
        locator = (By.XPATH, f'//a[contains(text(),"{name}")]')
        segment_page.find(locator)

    def test_delete_segment(self, auth):
        main_page = auth
        segment_page = main_page.go_to_segments()
        name = get_random_string(10)
        locator = (By.XPATH, f'//a[contains(text(),"{name}")]')
        segment_page.add_new_segment(name)
        segment_page.delete_segment(name)
        with pytest.raises(NoSuchElementException):
            segment_page.find(locator)

    def test_create_campaign(self, create_campaign):
        campaign_page, name = create_campaign
        locator = (By.XPATH, f'//a[contains(text(),"{name}")]')
        campaign_page.find(locator)
