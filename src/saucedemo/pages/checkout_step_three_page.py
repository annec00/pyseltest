from selenium.webdriver.common.by import By

from src.common.base_page import BasePage


class CheckoutStepThreePage(BasePage):
    """Represents the checkout step three page (Checkout Complete) of the SauceDemo application."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    GENERATE_PDF_BUTTON = (By.ID, "generate-pdf-order")

    # Other information
    URL_PATH = "checkout-complete.html"

    def __init__(self, driver):
        super().__init__(driver)
        self.page_title = "Checkout: Complete!"
        self.URL_PATH = "checkout-complete.html"

    def get_page_title(self) -> str:
        """Return the title of the checkout complete page."""
        return self.get_text(self.PAGE_TITLE)

    def get_complete_header(self) -> str:
        """Return the complete header text displayed on the checkout complete page."""
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self):
        """Click the 'Back Home' button to return to the home page."""
        self.click(self.BACK_HOME_BUTTON)

    def get_complete_text(self) -> str:
        """Return the complete text displayed on the checkout complete page."""
        return self.get_text(self.COMPLETE_TEXT)

    def click_generate_pdf(self):
        """Click the 'Generate PDF' button to generate a PDF of the order."""
        self.click(self.GENERATE_PDF_BUTTON)
