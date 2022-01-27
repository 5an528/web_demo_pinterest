import time
import pytest
from selenium.webdriver import Keys
from tests.base_test import BaseLoginTest
from data.test_data import TestData
from pages.post_page import PostPage
from pages.loginAndsignup_page import LoginSignupPage


class TestCase_005(BaseLoginTest):

    def test_tc_001(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.post_item_dot()
        time.sleep(5)
        log.info("System shows pop up page")

    def test_tc_002(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.post_item_share()
        time.sleep(5)
        log.info("System show pop up share page with different icon")

    def test_tc_003(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.post_item_love()
        time.sleep(5)
        log.info("System show change heart color to red")

    def test_tc_004(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.save()
        time.sleep(5)
        log.info("System show change save box color to black")

    def test_tc_005(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.follow()
        time.sleep(5)
        log.info("System show change follow box color to black with text")

    @pytest.mark.now
    def test_tc_006(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.comment()
        time.sleep(10)
        log.info("")  # Pr -----

    def test_tc_007(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.comment()
        time.sleep(5)
        log.info("")  # Pr -----

    def test_tc_008(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        postpage.post_item_love()
        time.sleep(5)
        log.info("System show change heart color to red")

    def test_tc_009(self):
        log = self.getLogger()
        postpage = PostPage(self.driver)
        postpage.post_item()
        time.sleep(5)
        log.info("No left right")
