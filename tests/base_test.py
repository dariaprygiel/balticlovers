import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.account_page import AccountPage, AccountPageLocators
from pages.home_page import HomePage, HomePageLocators
from pages.lavender_pareo_page import LavenderPareoPageLocators, LavenderPareoPage


class BaseTest(unittest.TestCase):
    """
    Base class for any test initialized on the home page
    """
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://balticlovers.pl/")
        self.driver.maximize_window()
        self.driver.find_element(*HomePageLocators.COOKIES_ACCEPT_BTN).click()
        self.driver.implicitly_wait(15)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()


class BaseTestAccount(unittest.TestCase):
    """
    Base class for any test initialized on the "My account" page
    """
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://balticlovers.pl/my-account/")
        self.driver.maximize_window()
        self.driver.find_element(*AccountPageLocators.COOKIES_ACCEPT_BTN).click()
        self.driver.implicitly_wait(15)
        self.register_page = AccountPage(self.driver)

    def tearDown(self):
        self.driver.quit()


class BaseTestProductPage(unittest.TestCase):
    """
    Base class for any test initialized on the product page WINDY PAREO LAVENDER JELLYFISH
    """
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://balticlovers.pl/product/windy-pareo-lavender-jellyfish/")
        self.driver.maximize_window()
        self.driver.find_element(*LavenderPareoPageLocators.COOKIES_ACCEPT_BTN).click()
        self.driver.implicitly_wait(15)
        self.product_page = LavenderPareoPage(self.driver)

    def tearDown(self):
        self.driver.quit()
