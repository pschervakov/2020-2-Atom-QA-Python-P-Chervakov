import os
import time

from locators.base_locators import CampaignPageLocators
from pages.base_page import BasePage


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    def upload_image(self):
        current_file_path = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(current_file_path, 'images', 'picture.jpg')
        el = self.find(self.locators.IMG_BUTTON)
        el.send_keys(image_path)

    def add_campaign(self, name):
        self.click(self.locators.TARGET_BUTTON)
        self.paste_into_form(self.locators.TARGET_FIELD, 'test.com')
        self.paste_into_form(self.locators.BUDGET_PER_DAY_FIELD, '100')
        self.paste_into_form(self.locators.FULL_BUDGET_FIELD, '100')
        self.click(self.locators.BANNER_BUTTON)
        self.upload_image()
        self.paste_into_form(self.locators.CAMPAIGN_NAME, name, clear=True)
        # creation failed with internal error if I don't do it
        time.sleep(1.5)
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def delete_all_campaigns(self):
        self.click(self.locators.CHECKBOX_ALL)
        self.click(self.locators.CAMPAIGN_ACTIONS)
        self.click(self.locators.remove_button, 10)
