from tests.base_test import BaseTest
from test_data.get_data import read_test_data_from_csv
from time import sleep
import unittest


class ContactFormTest(BaseTest):
    def test_contact_form_email_negative(self):
        """
        ID #003, #004, #005
        It tests the submission of the contact form - negative result, invalid email address
        """

        test_data = read_test_data_from_csv('/Users/dariaqa/PycharmProjects/newProject/test_data/contact_form_data.csv')
        for data in test_data:
            your_name = data['your_name']
            email = data['email']
            message = data['message']

        # Steps
        # 1. Navigate to the "Kontakt" page
        self.contact_page = self.home_page.open_contact_page()

        # 2. Verify that you are on the correct page
        assert "Kontakt" in self.driver.title

        # 3. Fill in the "Twoje imię" field
        self.contact_page.enter_your_name(your_name)

        # 4. Fill in the "Email" field
        self.contact_page.enter_email(email)

        # 5. Fill in the "Wiadomość" field
        self.contact_page.enter_message(message)

        # 6. Click the "Wyślij" button
        self.contact_page.submit_contact_form()

        # 7. Verify whether the message has been sent
        error_message = self.contact_page.return_error_message()
        expected_error_message = "Please enter a valid email address."
        self.assertEqual(error_message, "Please enter a valid email address.", "Error message does not match expected.")

        if error_message == expected_error_message:
            print("Test passed: the error message was displayed as expected, and the message was not sent.")
        else:
            print("Test failed: the error message was not as expected.")

        sleep(3)


if __name__ == "__main__":
    unittest.main()
