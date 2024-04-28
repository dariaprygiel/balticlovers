import unittest
from tests.contact_form_test import ContactFormTest
from tests.home_page_test import HomePageTest
from tests.new_order_test import PlaceOrderTest
from tests.product_page_test import ProductPageTest
from tests.registration_test import OpenRegisterPageTest


class TestSuite(unittest.TestSuite):
    """
    All tests for the e-commerce store Balticlovers.pl
    """

    def __init__(self):
        super().__init__()
        self.addTest(HomePageTest('test_home_page_load'))
        self.addTest(HomePageTest('test_new_items_carousel'))
        self.addTest(ContactFormTest('test_contact_form_email_negative'))
        self.addTest(ProductPageTest('test_add_product_to_wishlist'))
        self.addTest(ProductPageTest('test_add_same_product_to_cart'))
        self.addTest(OpenRegisterPageTest('test_open_registration_page'))
        self.addTest(OpenRegisterPageTest('test_register_account_weak_password'))
        self.addTest(PlaceOrderTest('test_place_order_negative'))


if __name__ == "__main__":
    unittest.main()
