from selenium.webdriver.common.by import By


class BasePageLocators:
    PROFILE_BUTTON = (By.XPATH, '//div[@class="right-module-rightButton-39YRvc right-module-mail-25NVA9"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[contains(@href,"logout")]')
    PROFILE_NAME = (By.XPATH, '//div[@class="right-module-userNameWrap-34ibLS"]')


class LoginPageLocators(BasePageLocators):
    ENTER_BUTTON = (By.XPATH, '//div[@class="responseHead-module-button-1BMAy4"]')
    LOGIN_BUTTON = (By.XPATH, '//div[@class="authForm-module-button-2G6lZu"]')
    MAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')


class MainPageLocators(BasePageLocators):
    CAMPAIGN_BUTTON2 = (By.XPATH, '//a[@href="/campaign/new"]')
    CAMPAIGN_BUTTON1 = (
        By.XPATH, '//div[@class="button-module-button-gYtDlg button-module-blue-1Bdz4L button-module-button-gYtDlg"]')

    SEGMENTS_BUTTON = (By.XPATH, '//a[@href="/segments"]')


class CampaignPageLocators(BasePageLocators):
    TARGET_BUTTON = (By.XPATH,
                     '//div[@class="column-list-item _traffic"]')
    TARGET_FIELD = (By.XPATH,
                    '//input[@placeholder="Введите ссылку"]')

    CAMPAIGN_NAME = (By.XPATH, '//*[@class="campaign-name__name-wrap js-campaign-name-wrap"]//input')

    BUDGET_PER_DAY_FIELD = (By.XPATH,
                            '//input[@data-test="budget-per_day"]')
    FULL_BUDGET_FIELD = (By.XPATH,
                         '//input[@data-test="budget-total"]')
    BANNER_BUTTON = (By.XPATH, '//span[@class="banner-format-item__title" and contains(text(), "Баннер")]')
    IMG_BUTTON = (By.XPATH,
                  '//input[@data-test="image_240x400"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH,
                              '//button[@cid="view515"]')

    CHECKBOX_ALL = (By.XPATH, '//input[@class="name-module-checkbox-JwyOc1 input-module-input-1xGLR8"]')

    CAMPAIGN_ACTIONS = (By.XPATH, '//div[@class="tableControls-module-selectItem-3PqVCC select-module-item-3gX1Mz"]')

    remove_button = (By.XPATH, '//li[contains(text(), "Удалить")]')


class SegmentPageLocators(BasePageLocators):
    SEGMENT1 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')

    SEGMENT2 = (By.XPATH, '//button[@class="button button_submit"]')
    CHEKBOX1 = (
        By.XPATH, '//input[@class="adding-segments-source__checkbox js-main-source-checkbox"]')
    SEGMENT_THEME = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    ADD_SEGMENT = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    SEGMENT_NAME_FIELD = (
        By.XPATH, '//div[@class="input input_create-segment-form"]//input[@class="input__inp js-form-element"]')

    CREATE_SEGMENT_FINALLY = (By.XPATH,
                              '//div[@class="button__text"]')
    CHECKBOX_ALL_SEGMENTS = (By.XPATH,
                             '//div[@class="segmentsTable-module-idHeaderCellWrap-2SRKat"]/input')

    SEGMENT_ACTIONS = (
        By.XPATH, '//div[@class="segmentsTable-module-selectItem-3thdV7 select-module-item-3gX1Mz"]')
    REMOVE_BUTTON = (By.XPATH, '//li[contains(text(), "Удалить")]')

    SEARCH_FIELD = (By.XPATH,
                    '//input[@class="suggester-module-searchInput-1dyLvN input-module-input-1xGLR8 suggester-module-withClearIcon-2DhXUT segmentsTable-module-suggester-qEovnR"]')
    SUGGESTED_RESULT = (By.XPATH, '//li[@class="suggester-module-option-1kQRIM optionsList-module-option-25VJZx"]')
