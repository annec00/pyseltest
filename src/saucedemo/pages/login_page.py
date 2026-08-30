from config.sauce_demo_config import BASE_URL
from src.common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    """Encapsulates the login page components and actions for the SauceDemo application."""

    # Locators for the login page elements
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL

    def load(self):
        """Load the login page."""
        self.open(self.url)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    