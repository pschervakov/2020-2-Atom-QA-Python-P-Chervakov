import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import base_locators

RETRY_COUNT = 5


class BasePage():
    locators = base_locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def paste_into_form(self, locator, query, clear=False, timeout=None):
        field = self.find(locator, timeout)
        if clear:
            field.clear()
        field.send_keys(query)

    def blind_click(self,*locators):
        def _blind_click(driver):
            for loc in locators:
                try:
                    element = EC.element_to_be_clickable(loc)(driver)
                    if element: return element
                except:
                    pass
            return False

        self.wait().until(_blind_click).click()

    def logout(self):
        self.click(self.locators.PROFILE_BUTTON)
        time.sleep(0.5)
        self.click(self.locators.LOGOUT_BUTTON)
