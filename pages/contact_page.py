from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPageLocators:
    YOUR_NAME = (By.ID, "wpforms-8163-field_0")
    EMAIL = (By.ID, "wpforms-8163-field_1")
    MESSAGE = (By.ID, "wpforms-8163-field_2")
    SUBMIT_BTN = (By.ID, "wpforms-submit-8163")
    EMAIL_ERROR = (By.ID, "wpforms-8163-field_1-error")


class ContactPage(BasePage):
    def enter_your_name(self, your_name):
        your_name_field = self.driver.find_element(*ContactPageLocators.YOUR_NAME)
        your_name_field.send_keys(your_name)

    def enter_email(self, email):
        email_field = self.driver.find_element(*ContactPageLocators.EMAIL)
        email_field.send_keys(email)

    def enter_message(self, message):
        message_field = self.driver.find_element(*ContactPageLocators.MESSAGE)
        message_field.send_keys(message)

    def submit_contact_form(self):
        form_submit = self.driver.find_element(*ContactPageLocators.SUBMIT_BTN)
        form_submit.click()

    def return_error_message(self):
        error_message = self.driver.find_element(*ContactPageLocators.EMAIL_ERROR)
        return error_message.text
