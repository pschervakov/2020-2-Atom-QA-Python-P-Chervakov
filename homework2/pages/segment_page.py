from locators.base_locators import SegmentPageLocators
from pages.base_page import BasePage


class SegmentPage(BasePage):
    locators = SegmentPageLocators()

    def add_new_segment(self, name):
        self.blind_click(self.locators.SEGMENT2, self.locators.SEGMENT1)
        self.click(self.locators.SEGMENT_THEME)
        self.click(self.locators.CHEKBOX1)
        self.click(self.locators.ADD_SEGMENT)
        self.paste_into_form(self.locators.SEGMENT_NAME_FIELD, name, True)
        self.click(self.locators.CREATE_SEGMENT_FINALLY)

    def delete_segment(self, name):
        self.paste_into_form(self.locators.SEARCH_FIELD, name)
        self.click(self.locators.SUGGESTED_RESULT)
        self.click(self.locators.CHECKBOX_ALL_SEGMENTS)
        self.click(self.locators.SEGMENT_ACTIONS)
        self.click(self.locators.REMOVE_BUTTON)

    def delete_all_segments(self):
        self.click(self.locators.CHECKBOX_ALL_SEGMENTS)
        self.click(self.locators.SEGMENT_ACTIONS)
        self.click(self.locators.REMOVE_BUTTON)
