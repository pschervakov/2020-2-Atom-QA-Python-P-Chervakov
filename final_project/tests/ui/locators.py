from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_USERNAME_FIELD = (By.XPATH, '//input[@class="uk-input uk-form-large"]')
    LOGIN_PASSWORD_FIELD = (By.XPATH, '//input[@class="uk-input uk-form-large uk-icon-eye"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@class="uk-button uk-button-primary uk-button-large uk-width-1-1"]')
    GO_TO_REG_BUTTON = (By.XPATH, '//a[@href="/reg"]')


class RegPageLocators:
    REG_USERNAME_FIELD = (By.XPATH, '//input[@class="uk-input uk-form-middle"]')
    REG_EMAIL_FIELD = (By.XPATH, '//input[@class="uk-input uk-form-midlle"]')
    REG_PASSWORD_FIELD = (By.XPATH, '//input[@class="uk-input uk-form-midlle uk-icon-eye"]')
    REG_REPEAT_PASSWORD_FIELD = (By.XPATH, '//input[@class="uk-input uk-form-middle uk-icon-eye"]')
    REG_CHECKBOX = (By.XPATH, '//input[@name="term"]')
    REG_BUTTON = (By.XPATH, '//input[@class="uk-button uk-button-primary uk-button-large uk-width-1-1"]')


class MainPageLocators:
    GO_TO_WHAT_API = (By.XPATH, '//img[@class="uk-overlay-scale"and @src="/static/images/laptop.png"]')
    GO_TO_FUTURE = (By.XPATH, '//img[@class="uk-overlay-scale"and @src="/static/images/loupe.png"]')
    GO_TO_SMTP = (By.XPATH, '//img[@class="uk-overlay-scale"and @src="/static/images/analytics.png"]')
    GO_TO_HOME = (By.XPATH, '//a[contains(text(),"HOME")]')
    GO_TO_PYTHON = (By.XPATH, '//li[@class="uk-parent"][a[contains(text(),"Python")]]')
    GO_TO_PYTHON_HISTORY = (By.XPATH, '//a[contains(text(),"Python history")]')
    GO_TO_FLASK = (By.XPATH, '//a[contains(text(),"Flask")]')
    LINUX = (By.XPATH, '//a[contains(text(),"Linux")]')
    GO_TO_CENTOS = (By.XPATH, '//a[contains(text(),"Centos7")]')
    NETWORK = (By.XPATH, '//a[contains(text(),"Network")]')
    GO_TO_WIRESHARK_NEWS = (By.XPATH, '//a[contains(text(),"News")]')
    GO_TO_WIRESHARK_DOWNLOAD = (By.XPATH, '//a[@href="https://www.wireshark.org/#download"]')
    GO_TO_TCP_EXAMPLES = (By.XPATH, '//a[contains(text(),"Examples")]')
    LOGOUT = (By.XPATH, '//a[@class="uk-button uk-button-danger"]')
