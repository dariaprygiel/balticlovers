from pages.lavender_pareo_page import LavenderPareoPage
from tests.base_test import BaseTestProductPage
from time import sleep
from test_data.get_data import read_test_data_from_csv
import unittest


class PlaceOrderTest(BaseTestProductPage):

    def test_place_order_negative(self, expected_error_message="Nieprawidłowy adres e-mail płatności"):
        """
        ID #013, #014, #015
        It tests the functionality of placing a new order - negative result, invalid email address
        """

        test_data = read_test_data_from_csv('/Users/dariaqa/PycharmProjects/newProject/test_data/checkout_data.csv')
        for data in test_data:
            name = data['name']
            surname = data['surname']
            street = data['street']
            postcode = data['postcode']
            city = data['city']
            phone_number = data['phone number']
            email = data['email']
            parcel_machine_number = data['parcel machine number']

        # Steps:
        # 1. Open the WINDY PAREO LAVENDER JELLYFISH product page
        self.product_page = LavenderPareoPage(self.driver)

        # 2. Click the "Dodaj do koszyka" button
        self.product_page.add_product_to_cart()

        # 3. Navigate to the cart page
        self.cart_page = self.product_page.view_cart()
        assert "Cart" in self.driver.title

        # 4. Navigate to the checkout page
        self.checkout_page = self.cart_page.go_to_checkout()
        assert "Checkout" in self.driver.title

        # 5. Fill in the "Imię" field
        self.checkout_page.enter_name(name)

        # 6. Fill in the "Nazwisko" field
        self.checkout_page.enter_surname(surname)

        # 7. Fill in the "Ulica" field
        self.checkout_page.enter_street(street)

        # 8. Fill in the "Kod pocztowy" field
        self.checkout_page.enter_postcode(postcode)

        # 9. Fill in the "Miasto" field
        self.checkout_page.enter_city(city)

        # 10. Fill in the "Numer telefonu" field
        self.checkout_page.enter_phone_number(phone_number)

        # 11. Fill in the "Adres e-mail" field
        self.checkout_page.enter_email(email)

        # 12. Search for a parcel machine to which the order is to be delivered
        self.checkout_page.search_parcel_machine(parcel_machine_number)
        sleep(5)

        # 13. Select the parcel machine from the list
        self.checkout_page.select_parcel_machine()

        # 14. Accept the terms and conditions of the store
        self.checkout_page.accept_terms()

        # 15. Click the "Kupuję i płacę" button
        self.checkout_page.place_order()

        # 16. Verify whether the order has been placed
        error_message = self.checkout_page.if_error_received()
        self.assertEqual(error_message, expected_error_message, "Error message does not match expected.")
        if error_message == expected_error_message:
            print("Order has not been placed due to an invalid e-mail address")

        sleep(3)


if __name__ == "__main__":
    unittest.main()
