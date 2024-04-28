from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WishlistPageLocators:
    WISHLISTED_ITEM_NAME = (By.CSS_SELECTOR, "div.woosw-item--name > a")


class WishlistPage(BasePage):
    def get_wishlisted_item_name(self):
        wishlisted_item = self.driver.find_element(*WishlistPageLocators.WISHLISTED_ITEM_NAME)
        item_name = wishlisted_item.text
        print(item_name, "is on the Wishlist.")
