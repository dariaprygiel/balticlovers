from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.contact_page import ContactPage
from pages.account_page import AccountPage


class HomePageLocators:
    COOKIES_ACCEPT_BTN = (By.ID, "wt-cli-accept-all-btn")
    CONTACT_BTN = (By.XPATH, "//a[@href='https://balticlovers.pl/kontakt/'][text()='Kontakt']")
    ACCOUNT_BTN = (By.CLASS_NAME, "ekommart-icon-user")


class HomePage(BasePage):

    def open_contact_page(self):
        contact = self.driver.find_element(*HomePageLocators.CONTACT_BTN)
        contact.click()
        return ContactPage(self.driver)

    def open_account_page(self):
        account = self.driver.find_element(*HomePageLocators.ACCOUNT_BTN)
        account.click()
        return AccountPage(self.driver)
