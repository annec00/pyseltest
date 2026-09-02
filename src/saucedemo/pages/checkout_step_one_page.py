from selenium.webdriver.common.by import By

from src.common.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Represents the checkout page of the SauceDemo application."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Other information
    URL_PATH = "checkout-step-one.html"
    TITLE = "Checkout: Your Information"

    def __init__(self, driver):
        super().__init__(driver)
        self.page_title = "Checkout: Your Information"
        self.URL_PATH = "checkout-step-one.html"

    def get_page_title(self) -> str:
        """Return the title of the checkout page."""
        return self.get_text(self.PAGE_TITLE)

    def enter_first_name(self, first_name: str):
        """Enter the first name in the checkout form."""
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str):
        """Enter the last name in the checkout form."""
        self.type(self.LAST_NAME_INPUT, last_name)

    def enter_zip_code(self, zip_code: str):
        """Enter the zip code in the checkout form."""
        self.type(self.ZIP_CODE_INPUT, zip_code)

    def click_continue(self):
        """Click the continue button to proceed to the next step."""
        self.click(self.CONTINUE_BUTTON)

    def click_cancel(self):
        """Click the cancel button to return to the cart page."""
        self.click(self.CANCEL_BUTTON)
