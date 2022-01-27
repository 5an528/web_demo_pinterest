import time
from utilities.locators import *
from pages.base_page import BasePage
from data.test_data import TestData


class HomeTwoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = HomePageLocators

    def logo_btn(self):
        return self.driver.find_element(*self.locators.LOGO)

    def home_btn(self):
        return self.driver.find_element(*self.locators.HOME)

    def search(self):
        return self.driver.find_element(*self.locators.SEARCH)

    def notifications(self):
        return self.driver.find_element(*self.locators.NOTIFICATION)

    def messages(self):
        return self.driver.find_element(*self.locators.MESSAGES)

    def profile(self):
        return self.driver.find_element(*self.locators.PROFILE)

    def messages_box(self):
        return self.driver.find_element(*self.locators.MESSAGES_BOX)

    def profile_button(self):
        return self.driver.find_element(*self.locators.PROFILE_BUTTON)

    def profile_edit_button(self):
        return self.driver.find_element(*self.locators.PROFILE_EDIT_BUTTON)

    def profile_share_button(self):
        return self.driver.find_element(*self.locators.PROFILE_SHARE_BUTTON)

    def question_button(self):
        return self.driver.find_element(*self.locators.QUESTION_MARK).click()

    def visit_help(self):
        return self.driver.find_element(*self.locators.VISIT_HELP_CENTER).click()

    def about(self):
        return self.driver.find_element(*self.locators.ABOUT).click()

    def plus(self):
        return self.wait_element(*self.locators.PLUS)

    def create_pin(self):
        return self.driver.find_element(*self.locators.CREATE_PIN).click()

    def get_browser(self):
        return self.driver.find_element(*self.locators.GET_OUR_BROWSER).click()
