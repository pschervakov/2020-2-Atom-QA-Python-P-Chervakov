from locators.base_locators import MainPageLocators
from pages.base_page import BasePage
from pages.campaign_page import CampaignPage
from pages.segment_page import SegmentPage


class MainPage(BasePage):
    locators = MainPageLocators

    def go_to_campaigns(self):
        self.blind_click(self.locators.CAMPAIGN_BUTTON1, self.locators.CAMPAIGN_BUTTON2)
        return CampaignPage(self.driver)

    def go_to_segments(self):
        self.click(self.locators.SEGMENTS_BUTTON)
        return SegmentPage(self.driver)
