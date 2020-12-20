from tests.ui.pages.base_page import BasePage
from tests.ui.locators import MainPageLocators
from selenium.webdriver import ActionChains

expected_titles = [('python', 'Welcome to Python.org'),
                   ('python_history', 'History of Python'), ('flask', 'Flask'),
                   ('wireshark_news', 'Wireshark · News'),
                   ('wireshark_download', 'Wireshark · Go Deep.'),
                   ('tcp_examples', 'Tcpdump Examples'), ('API', 'API'),
                   ('future', 'What Will the Internet'), ('SMTP', 'SMTP')]


class MainPage(BasePage):
    locators = MainPageLocators()

    def logout(self):
        self.click(self.locators.LOGOUT)

    def go_to(self, type_):
        if type_ == 'python':
            self.click(self.locators.GO_TO_PYTHON)
        elif type_ == 'python_history':
            self.hover_and_click(menu_locator=self.locators.GO_TO_PYTHON,
                                 submenu_locator=self.locators.GO_TO_PYTHON_HISTORY)

        elif type_ == 'flask':
            self.hover_and_click(menu_locator=self.locators.GO_TO_PYTHON, submenu_locator=self.locators.GO_TO_FLASK)
        elif type_ == 'centos':
            self.hover_and_click(menu_locator=self.locators.LINUX, submenu_locator=self.locators.GO_TO_CENTOS)

        elif type_ == 'wireshark_news':
            self.hover_and_click(menu_locator=self.locators.NETWORK, submenu_locator=self.locators.GO_TO_WIRESHARK_NEWS)

        elif type_ == 'wireshark_download':
            self.hover_and_click(menu_locator=self.locators.NETWORK,
                                 submenu_locator=self.locators.GO_TO_WIRESHARK_DOWNLOAD)

        elif type_ == 'tcp_examples':
            self.hover_and_click(menu_locator=self.locators.NETWORK, submenu_locator=self.locators.GO_TO_TCP_EXAMPLES)

        elif type_ == 'API':
            self.click(self.locators.GO_TO_WHAT_API)
        elif type_ == 'future':
            self.click(self.locators.GO_TO_FUTURE)
        elif type_ == 'SMTP':
            self.click(self.locators.GO_TO_SMTP)

    def check_title(self, text):
        return text in self.driver.title
    
