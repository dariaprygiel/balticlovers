from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPageLocators:
    COOKIES_ACCEPT_BTN = (By.ID, "wt-cli-accept-all-btn")
    EMAIL_FIELD = (By.ID, "reg_email")
    PASSWORD_FIELD = (By.ID, "reg_password")
    CREATE_ACCOUNT_BTN = (By.CLASS_NAME, "woocommerce-form-register__submit")
    PASSWORD_ERROR = (By.CLASS_NAME, "woocommerce-password-strength")


class AccountPage(BasePage):
    def enter_email(self, email):
        email_field = self.driver.find_element(*AccountPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(*AccountPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def return_password_error_message(self):
        password_error_message = self.driver.find_element(*AccountPageLocators.PASSWORD_ERROR)
        return password_error_message.text

    def if_register_btn_disabled(self):
        register_btn = (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                             (AccountPageLocators.CREATE_ACCOUNT_BTN)))
        if "disabled" in register_btn.get_attribute("class"):
            print("Button is not clickable (it is disabled)")
        else:
            print("Button is clickable")
