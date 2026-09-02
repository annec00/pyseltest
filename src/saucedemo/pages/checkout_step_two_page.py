from selenium.webdriver.common.by import By

from src.common.base_page import BasePage
from src.saucedemo.components.cart_item import CartItem


class CheckoutStepTwoPage(BasePage):
    """Represents the checkout page of the SauceDemo application."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    PAYMENT_INFO = (By.CLASS_NAME, "summary_value_label")
    SHIPPING_INFO = (By.CLASS_NAME, "summary_value_label")
    PRICE_TOTAL_ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    PRICE_TAX = (By.CLASS_NAME, "summary_tax_label")
    PRICE_TOTAL = (By.CLASS_NAME, "summary_total_label")

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

    def click_finish(self):
        """Click the finish button to complete the checkout process."""
        self.click(self.FINISH_BUTTON)

    def click_cancel(self):
        """Click the cancel button to return to the cart page."""
        self.click(self.CANCEL_BUTTON)

    def get_payment_info(self) -> str:
        """Return the payment information displayed on the checkout page."""
        return self.get_text(self.PAYMENT_INFO)

    def get_shipping_info(self) -> str:
        """Return the shipping information displayed on the checkout page."""
        return self.get_text(self.SHIPPING_INFO)

    def get_price_total_item_total(self) -> str:
        """Return the item total price displayed on the checkout page."""
        return self.get_text(self.PRICE_TOTAL_ITEM_TOTAL)

    def get_price_tax(self) -> str:
        """Return the tax price displayed on the checkout page."""
        return self.get_text(self.PRICE_TAX)

    def get_price_total(self) -> str:
        """Return the total price displayed on the checkout page."""
        return self.get_text(self.PRICE_TOTAL)

    # get CartItems
    def get_cart_items(self) -> list[CartItem]:
        """Return a list of CartItem components for every row in the cart."""
        return [CartItem(el) for el in self.find_all(self.CART_ITEMS)]
