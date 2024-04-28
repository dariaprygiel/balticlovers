from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage


class CartPageLocators:
    CHECKOUT_BTN = (By.CLASS_NAME, "wc-proceed-to-checkout")
    QUANTITY_VALUE = (By.CLASS_NAME, "input-text.qty")


class CartPage(BasePage):
    def go_to_checkout(self):
        open_checkout = self.driver.find_element(*CartPageLocators.CHECKOUT_BTN)
        open_checkout.click()
        return CheckoutPage(self.driver)

    def get_quantity(self):
        quantity = self.driver.find_element(*CartPageLocators.QUANTITY_VALUE)
        return quantity.get_attribute("value")

    def validate_quantity(self, expected_quantity):
        quantity = self.get_quantity()
        if quantity == str(expected_quantity):
            print("Correct quantity:", quantity)
        else:
            print("Incorrect quantity. Expected:", expected_quantity, "Actual:", quantity)
