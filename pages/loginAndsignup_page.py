import time

from utilities.locators import *
from pages.base_page import BasePage
from data.test_data import TestData


class LoginSignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignupLoginPageLocators
        self.ads_locators = AdsPageLocators

    # Login Signup button in homepage
    def login_btn(self):
        return self.driver.find_element(*self.locators.LOGIN_BUTTON)

    def signup_btn(self):
        return self.driver.find_element(*self.locators.SIGN_UP_BUTTON)

    # Login/Signup with Email & Pass input

    def login(self):
        email_filed = self.driver.find_element(*self.locators.EMAIL_INPUT)
        email_filed.clear()
        email_filed.send_keys(TestData.DEMO_EMAIL)
        pass_field = self.driver.find_element(*self.locators.PASS_INPUT)
        pass_field.clear()
        pass_field.send_keys(TestData.DEMO_PASS)
        self.driver.find_element(*self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)

    def signup(self):
        email_filed = self.driver.find_element(*self.locators.EMAIL_INPUT)
        email_filed.clear()
        time.sleep(2)
        email_filed.send_keys(TestData.DEMO_EMAIL)
        pass_field = self.driver.find_element(*self.locators.PASS_INPUT)
        pass_field.clear()
        time.sleep(2)
        pass_field.send_keys(TestData.DEMO_PASS)
        age_field = self.driver.find_element(*self.locators.AGE_INPUT)
        age_field.clear()
        age_field.send_keys(TestData.DEMO_AGE)
        time.sleep(2)
        self.driver.find_element(*self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)

    def profile(self):
        profile = self.driver.find_element(*self.ads_locators.PROFILE)
        return profile

    # Login/Signup with Facebook & Google

    def fb_btn(self):
        return self.driver.find_element(*self.locators.FB_BUTTON)

    def login_fb(self):
        main_page = self.driver.current_window_handle
        self.driver.find_element(*self.locators.FB_BUTTON).click()
        self.driver.implicitly_wait(10)
        for handle in self.driver.window_handles:
            if handle != main_page:
                fb_login = handle
                self.driver.switch_to.window(fb_login)
        fb_email_field = self.driver.find_element(*self.locators.FB_EMAIL)
        fb_email_field.clear()
        time.sleep(2)
        fb_email_field.send_keys(TestData.DEMO_EMAIL)
        fb_pass_field = self.driver.find_element(*self.locators.FB_PASS)
        fb_pass_field.clear()
        time.sleep(2)
        fb_pass_field.send_keys(TestData.DEMO_PASS)
        time.sleep(2)
        self.driver.find_element(*self.locators.FB_SUBMIT).click()
        time.sleep(5)
        self.driver.switch_to.window(main_page)

    def g_btn(self):
        return self.driver.find_element(*self.locators.G_BUTTON)
