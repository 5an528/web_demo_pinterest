from utilities.locators import *
from pages.base_page import BasePage


class PostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = PostPageLocators

    def post_item(self):
        items = self.driver.find_elements(*self.locator.POST_ITEM)
        return items[0].click()

    def post_item_dot(self):
        dots = self.driver.find_elements(*self.locator.POST_DOT)
        return dots[0].click()

    def post_item_share(self):
        dots = self.driver.find_elements(*self.locator.POST_SHARE)
        return dots[-1].click()

    def post_item_love(self):
        love = self.driver.find_elements(*self.locator.POST_LOVE)
        return love[0].click()

    def save(self):
        save = self.driver.find_element(*self.locator.SAVE)
        return save.click()

    def follow(self):
        follow = self.driver.find_element(*self.locator.FOLLOW)
        return follow.click()

    def comment(self):
        comment = self.wait_element(*self.locator.COMMENT)
        comment.clear()
        comment.send_keys("asd")