from pages.account_page import AccountPage
from tests.base_test import BaseTest, BaseTestAccount
from time import sleep
from test_data.get_data import read_test_data_from_csv
import unittest


class OpenRegisterPageTest(BaseTest):
    def test_open_registration_page(self):
        """
        ID #008
        It tests whether the registration page loads successfully
        """
        # Steps:
        # 1. Open the home page of the BALTICLOVERS store
        # 2. Click on the user icon in the menu to the right
        self.register_page = self.home_page.open_account_page()

        # 3. Verify that you are on the correct page
        assert "My account" in self.driver.title

        sleep(3)


class RegisterAccountTest(BaseTestAccount):
    def test_register_account_weak_password(self, expected_error_message="Słabe - Proszę wpisać mocniejsze hasło."):
        """
        ID #009, #010, #011, #012
        It tests the functionality of registering a new user account - negative result, weak password
        """

        test_data = read_test_data_from_csv('/Users/dariaqa/PycharmProjects/newProject/test_data/registration_data.csv')
        for data in test_data:
            email = data['email']
            password = data['password']

        # Steps:
        # 1. Navigate to the "My account" page
        self.register_page = AccountPage(self.driver)

        # 2. Verify that you are on the correct page
        assert "My account" in self.driver.title

        # 3. Fill in the "Adres email" field
        self.register_page.enter_email(email)

        # 4. Fill in the "Hasło" field
        self.register_page.enter_password(password)

        # 5. Verify whether the account can be registered
        self.register_page.if_register_btn_disabled()
        error_message = self.register_page.return_password_error_message()
        self.assertEqual(error_message, expected_error_message, "Error message does not match expected.")
        if error_message == expected_error_message:
            print("Account can't be registered, password is too weak")

        sleep(3)


if __name__ == "__main__":
    unittest.main()
