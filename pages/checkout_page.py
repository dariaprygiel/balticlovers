from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.order_confirmation_page import OrderConfirmationPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPageLocators(BasePage):
    NAME_FIELD = (By.ID, "billing_first_name")
    SURNAME_FIELD = (By.ID, "billing_last_name")
    STREET_FIELD = (By.ID, "billing_address_1")
    POSTCODE_FIELD = (By.ID, "billing_postcode")
    CITY_FIELD = (By.ID, "billing_city")
    PHONE_NUMBER_FIELD = (By.ID, "billing_phone")
    EMAIL_FIELD = (By.ID, "billing_email")
    PARCEL_MACHINE_SEARCH = (By.XPATH, "//span[@class='select2-selection__placeholder'and text()='Wpisz miasto lub "
                                       "miasto, ulica.']")
    PARCEL_MACHINE_INPUT = (By.XPATH, "//input[@class='select2-search__field']")
    PARCEL_MACHINE_LISTED = (By.XPATH, "//span[@class='select2-results']//li")
    TERMS_CHECKBOX = (By.ID, "terms")
    PLACE_ORDER_BTN = (By.ID, "place_order")
    EMAIL_ERROR_MESSAGE = (By.CLASS_NAME, 'woocommerce-error')


class CheckoutPage(BasePage):
    def enter_name(self, name):
        name_field = self.driver.find_element(*CheckoutPageLocators.NAME_FIELD)
        name_field.send_keys(name)

    def enter_surname(self, surname):
        surname_field = self.driver.find_element(*CheckoutPageLocators.SURNAME_FIELD)
        surname_field.send_keys(surname)

    def enter_street(self, street):
        street_field = self.driver.find_element(*CheckoutPageLocators.STREET_FIELD)
        street_field.send_keys(street)

    def enter_postcode(self, postcode):
        postcode_field = self.driver.find_element(*CheckoutPageLocators.POSTCODE_FIELD)
        postcode_field.send_keys(postcode)

    def enter_city(self, city):
        city_field = self.driver.find_element(*CheckoutPageLocators.CITY_FIELD)
        city_field.send_keys(city)

    def enter_phone_number(self, phone_number):
        phone_number_field = self.driver.find_element(*CheckoutPageLocators.PHONE_NUMBER_FIELD)
        phone_number_field.send_keys(phone_number)

    def enter_email(self, email):
        email_field = self.driver.find_element(*CheckoutPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def search_parcel_machine(self, parcel_machine_number):
        wait = WebDriverWait(self.driver, 10)
        parcel_machine_search = wait.until(EC.element_to_be_clickable(CheckoutPageLocators.PARCEL_MACHINE_SEARCH))
        parcel_machine_search.click()
        parcel_machine_input = wait.until(EC.element_to_be_clickable(CheckoutPageLocators.PARCEL_MACHINE_INPUT))
        parcel_machine_input.send_keys(parcel_machine_number)

    def select_parcel_machine(self):
        parcel_machine = self.driver.find_element(*CheckoutPageLocators.PARCEL_MACHINE_LISTED)
        parcel_machine.click()

    def accept_terms(self):
        terms_checkbox = self.driver.find_element(*CheckoutPageLocators.TERMS_CHECKBOX)
        terms_checkbox.click()

    def place_order(self):
        place_order = self.driver.find_element(*CheckoutPageLocators.PLACE_ORDER_BTN)
        place_order.click()
        return OrderConfirmationPage(self.driver)

    def if_error_received(self):
        error_message = self.driver.find_element(*CheckoutPageLocators.EMAIL_ERROR_MESSAGE)
        return error_message.text
