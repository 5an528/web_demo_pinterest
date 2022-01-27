from utilities.locators import *
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators

    def homepage(self):
        return self.driver

    def find_logo_text(self):
        self.wait_element(*self.locator.LOGO_TEXT)
        text_element = self.driver.find_element(*self.locator.LOGO_TEXT)
        text = text_element.text
        return text
