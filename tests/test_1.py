import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCase_001(BaseTest):
    def test_tc_001_loadsite(self):
        home_page = HomePage(self.driver)
        log = self.getLogger()
        text = home_page.find_logo_text()
        assert text == "Pinterest"
        log.info("System show the home page")


