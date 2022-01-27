import time
import pytest
from tests.base_test import BaseTest
from data.test_data import TestData
from pages.loginAndsignup_page import LoginSignupPage


# Signup
class TestCase_003(BaseTest):
    # Email Signup
    def test_tc_001(self):
        signup_by_email = LoginSignupPage(self.driver)
        log = self.getLogger()
        signup_by_email.signup_btn().click()
        signup_by_email.signup()
        time.sleep(2)
        # signup_by_email.profile().is_displayed()
        log.info("System show the home page with login profile")

    # FB Signup
    def test_tc_002(self):
        login_and_signup_by_fb = LoginSignupPage(self.driver)
        log = self.getLogger()
        login_and_signup_by_fb.login_btn().click()
        login_and_signup_by_fb.login_fb()
        login_and_signup_by_fb.profile().is_displayed()
        log.info("System show the home page with login profile")

    # Google Signup
    def test_tc_003(self):
        login_and_signup_by_google = LoginSignupPage(self.driver)
        log = self.getLogger()
        login_and_signup_by_google.login_btn().click()
        login_and_signup_by_google.g_btn().click()
        time.sleep(5)
        log.info("Continue with Google Popup Problem")
        # ____ Continue with Google Popup Problem ____STEP3***
