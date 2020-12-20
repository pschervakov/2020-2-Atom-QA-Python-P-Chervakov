from tests.ui.pages.base_page import BasePage
from tests.ui.locators import RegPageLocators


class RegPage(BasePage):
    locators = RegPageLocators()

    def reg(self, user, password, email, rpassword=None):
        if rpassword is None:
            rpassword = password
        self.paste_into_form(self.locators.REG_USERNAME_FIELD, query=user)
        self.paste_into_form(self.locators.REG_EMAIL_FIELD, query=email)
        self.paste_into_form(self.locators.REG_PASSWORD_FIELD, query=password)
        self.paste_into_form(self.locators.REG_REPEAT_PASSWORD_FIELD, query=rpassword)
        self.click(self.locators.REG_CHECKBOX)
        self.click(self.locators.REG_BUTTON)
