from locators.base_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def go_to_login_window(self):
        self.click(self.locators.ENTER_BUTTON)

    def login(self, mail, password):
        self.go_to_login_window()
        login = self.find(self.locators.MAIL_FIELD)
        login.send_keys(mail)
        password_field = self.find(self.locators.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)
        return BasePage(self.driver)


