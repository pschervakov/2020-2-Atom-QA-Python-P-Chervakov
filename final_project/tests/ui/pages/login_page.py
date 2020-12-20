from tests.ui.pages.base_page import BasePage
from tests.ui.locators import LoginPageLocators
from tests.settings import APP_URl, ADMIN_USER, ADMIN_PASS


class LoginPage(BasePage):
    locators = LoginPageLocators

    def go_to_reg_page(self):
        self.click(locator=self.locators.GO_TO_REG_BUTTON)

    def login(self, user=ADMIN_USER, password=ADMIN_PASS):
        self.paste_into_form(locator=self.locators.LOGIN_USERNAME_FIELD, query=user)
        self.paste_into_form(locator=self.locators.LOGIN_PASSWORD_FIELD, query=password)
        self.click(locator=self.locators.LOGIN_BUTTON)

    def is_instance(self):
        return self.driver.current_url == f'{APP_URl}/login'
