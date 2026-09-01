from selenium.webdriver.common.by import By

from config.sauce_demo_config import BASE_URL
from src.common.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates the login page components and actions for the SauceDemo application."""

    # Locators for the login page elements
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL

    def open_page(self):
        """Open the login page."""
        self.driver.get(self.url)

    def wait_for_page_load(self):
        """Load the login page."""
        self.wait_for_visible(self.LOGO)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def login(self, username, password):
        """Perform the login action with the provided username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
