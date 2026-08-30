from selenium.webdriver.common.by import By

from src.common.base_page import BasePage


class HomePage(BasePage):

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self, timeout=10):
        """Wait for the home page to load by checking the visibility of the page title."""
        self.wait_for_visible(self.PAGE_TITLE)

    def get_page_title(self):
        """Get the title of the home page."""
        return self.get_text(self.PAGE_TITLE)
