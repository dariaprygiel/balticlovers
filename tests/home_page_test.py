from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from time import sleep
import unittest


class HomePageTest(BaseTest):
    def test_home_page_load(self):
        """
        ID #001
        It tests whether the home page loads properly
        """

        # Steps:
        # 1. Open a browser
        # 2. Enter the URL of the home page for the online store:: https://balticlovers.pl/
        # 3. Verify that you are on the correct page
        assert "Ahoj" in self.driver.title

        sleep(3)

    def test_new_items_carousel(self):
        """
        ID #002
        It tests whether the BOSMAN HOODIE BLACK product displays in the default carousel view under the header
        NOWOŚCI W BALTICLOVERS
        """

        # Steps:
        # 1. Open a browser
        # 2. Enter the URL of the home page for the online store:: https://balticlovers.pl/
        # 3. Find the carousel element
        self.carousel = self.driver.find_element(By.ID, "elementor-tab-title-3021")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.carousel)

        # 4. Verify whether the carousel displays the product BOSMAN HOODIE BLACK
        try:
            product_link = self.carousel.find_element(By.XPATH, '//a[text()="Bosman hoodie black"]')
            product_text = product_link.text.strip()
            if product_text:
                print(product_text, "is visible in the default carousel view.")
            else:
                print("This item is not visible in the default carousel view.")
        except NoSuchElementException:
            print("Product element not found in the carousel.")

        sleep(3)


if __name__ == "__main__":
    unittest.main()
