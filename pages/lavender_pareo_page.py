from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.cart_page import CartPage
from pages.wishlist_page import WishlistPage


class LavenderPareoPageLocators:
    COOKIES_ACCEPT_BTN = (By.ID, "wt-cli-accept-all-btn")
    ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, "button.woosw-btn.woosw-btn-15364")
    OPEN_WISHLIST_BTN = (By.CLASS_NAME, "woosw-page")
    ADD_TO_CART_BTN = (By.NAME, "add-to-cart")
    CONFIRMATION_MSG = (By.XPATH, "//div[@class='woocommerce-message']")
    VIEW_CART_BTN = (By.XPATH, '//*[@id="content"]/div/div[1]/div/a')


class LavenderPareoPage(BasePage):
    def add_product_to_wishlist(self):
        add_to_wishlist = self.driver.find_element(*LavenderPareoPageLocators.ADD_TO_WISHLIST_BTN)
        add_to_wishlist.click()

    def open_wishlist(self):
        open_wishlist = self.driver.find_element(*LavenderPareoPageLocators.OPEN_WISHLIST_BTN)
        self.driver.execute_script("arguments[0].click();", open_wishlist)
        return WishlistPage(self.driver)

    def add_product_to_cart(self):
        add_to_cart = self.driver.find_element(*LavenderPareoPageLocators.ADD_TO_CART_BTN)
        add_to_cart.click()
        return self

    def is_product_added_to_cart(self):
        confirmation = self.driver.find_element(*LavenderPareoPageLocators.CONFIRMATION_MSG)
        assert "został dodany do koszyka" in confirmation.text

    def view_cart(self):
        view_cart = self.driver.find_element(*LavenderPareoPageLocators.VIEW_CART_BTN)
        view_cart.click()
        return CartPage(self.driver)
