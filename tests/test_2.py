import time

import pytest

from tests.base_test import BaseTest
from data.test_data import TestData
from pages.loginAndsignup_page import LoginSignupPage


# Login
class TestCase_002(BaseTest):
    # Email Login
    def test_tc_001(self):
        login_by_email = LoginSignupPage(self.driver)
        log = self.getLogger()
        login_by_email.login_btn().click()
        login_by_email.login()
        time.sleep(2)
        login_by_email.profile().is_displayed()
        log.info("System show the home page with login profile")

    # FB Login
    def test_tc_002(self):
        login_by_fb = LoginSignupPage(self.driver)
        log = self.getLogger()
        login_by_fb.login_btn().click()
        login_by_fb.login_fb()
        login_by_fb.profile().is_displayed()
        log.info("System show the home page with login profile")

    # Google Login
    def test_tc_003(self):
        login_by_google = LoginSignupPage(self.driver)
        log = self.getLogger()
        login_by_google.login_btn().click()
        login_by_google.g_btn().click()
        time.sleep(5)
        log.info("Continue with Google Popup Problem")
        # ____ Continue with Google Popup Problem ____STEP3***
