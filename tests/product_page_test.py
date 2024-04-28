from pages.lavender_pareo_page import LavenderPareoPage
from tests.base_test import BaseTestProductPage
from time import sleep
import unittest


class ProductPageTest(BaseTestProductPage):
    def test_add_product_to_wishlist(self):
        """
        ID #006
        It tests the functionality of adding a product to the Wishlist
        """

        # Steps:
        # 1. Open the WINDY PAREO LAVENDER JELLYFISH product page
        self.product_page = LavenderPareoPage(self.driver)

        # 2. Verify that you are on the correct page
        assert "jellyfish" in self.driver.title

        # 3. Click the "Add to wishlist" button
        self.product_page.add_product_to_wishlist()

        # 4. Click the "Open wishlist page" button
        self.wishlist_page = self.product_page.open_wishlist()

        # 5. Verify that you are on the correct page
        assert "Wishlist" in self.driver.title

        # 6. Verify whether the WINDY PAREO LAVENDER JELLYFISH is on the Wishlist
        self.wishlist_page.get_wishlisted_item_name()

        sleep(3)

    def test_add_same_product_to_cart(self):
        """
        ID #007
        It tests whether the number of items in the cart increases when the same item is added to the cart again
        """

        # Steps:
        # 1. Open the WINDY PAREO LAVENDER JELLYFISH product page
        self.product_page = LavenderPareoPage(self.driver)

        # 2. Verify that you are on the correct page
        assert "jellyfish" in self.driver.title

        # 3. Click the "Dodaj do koszyka" button
        self.product_page.add_product_to_cart()

        # 4. Confirm that the product has been added to the cart
        self.product_page.is_product_added_to_cart()

        # 5. Navigate to the cart page
        self.cart_page = self.product_page.view_cart()
        assert "Cart" in self.driver.title

        # 6. Verify that the product WINDY PAREO LAVENDER JELLYFISH is in the cart in quantity of 1
        self.cart_page.validate_quantity(1)

        # 7. Return to the WINDY PAREO LAVENDER JELLYFISH product page
        self.driver.back()
        assert "Windy pareo lavender jellyfish" in self.driver.title

        # 8. Click the "Dodaj do koszyka" button again
        self.product_page.add_product_to_cart()

        # 9. Confirm that the product has been added to the cart
        self.product_page.is_product_added_to_cart()

        # 10. Navigate to the cart page
        self.cart_page = self.product_page.view_cart()
        assert "Cart" in self.driver.title

        # 11. Verify that the product WINDY PAREO LAVENDER JELLYFISH is in the cart in quantity of 2
        self.cart_page.validate_quantity(2)

        sleep(3)


if __name__ == "__main__":
    unittest.main()
