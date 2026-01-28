from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_inventory_displayed(self):
        return self.driver.find_element(*self.INVENTORY_CONTAINER).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
