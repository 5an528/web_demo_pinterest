import time
import pytest
from selenium.webdriver import Keys
from tests.base_test import BaseLoginTest
from data.test_data import TestData
from pages.home_two_page import HomeTwoPage
from pages.loginAndsignup_page import LoginSignupPage


class TestCase_004(BaseLoginTest):
    # Logo
    def test_tc_001(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.logo_btn().click()
        log.info("System shows the home page")

    # Home
    def test_tc_002(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.home_btn().click()
        log.info("System shows the home page")

    # Search
    def test_tc_003(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.search().send_keys("Avatar", Keys.ENTER)
        time.sleep(10)
        log.info("System shows the result")

    def test_tc_004(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.notifications().click()
        time.sleep(5)
        log.info("System pop up the notification page")  # -----------------no notification #

    def test_tc_005(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        self.driver.implicitly_wait(10)
        homepage.messages().click()
        homepage.profile().click()
        homepage.messages_box().send_keys("Hello, How are you?", Keys.ENTER)
        time.sleep(5)
        log.info("System pop up message page and reply message")

    def test_tc_006(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.profile_button().click()
        time.sleep(2)
        homepage.profile_edit_button().click()
        time.sleep(2)
        log.info("System show profile page")

    def test_tc_007(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.profile_button().click()
        time.sleep(2)
        homepage.profile_share_button().click()
        log.info("System show profile page")
        time.sleep(5)

    def test_tc_008(self):
        log = self.getLogger()
        main_page = self.driver.current_window_handle
        homepage = HomeTwoPage(self.driver)
        time.sleep(5)
        homepage.question_button()
        time.sleep(2)
        log.info("Successfully click Question")
        homepage.about()
        for handle in self.driver.window_handles:
            if handle != main_page:
                about = handle
                self.driver.switch_to.window(about)
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(main_page)
        time.sleep(2)
        log.info("System show pop up page with others option")

    def test_tc_009(self):
        log = self.getLogger()
        main_page = self.driver.current_window_handle
        homepage = HomeTwoPage(self.driver)
        time.sleep(5)
        homepage.question_button()
        time.sleep(2)
        homepage.about()
        for handle in self.driver.window_handles:
            if handle != main_page:
                about = handle
                self.driver.switch_to.window(about)
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(main_page)
        time.sleep(2)
        log.info("System show pop up page with others option")

    def test_tc_0010(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.plus().click()
        time.sleep(1)
        homepage.create_pin().click()
        time.sleep(1)
        log.info("System show pop up page with others option")

    def test_tc_0011(self):
        log = self.getLogger()
        homepage = HomeTwoPage(self.driver)
        homepage.plus().click()
        time.sleep(1)
        homepage.get_browser()
        time.sleep(1)
        log.info("System show pop up page with others option")
