from selenium.webdriver.common.by import By

from src.common.base_page import BasePage
from src.saucedemo.components.cart_item import CartItem


class CartPage(BasePage):
    """Represents the cart page of the SauceDemo application."""

    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_items_locator = self.CART_ITEMS
        self.checkout_button_locator = self.CHECKOUT_BUTTON
        self.continue_shopping_button_locator = self.CONTINUE_SHOPPING_BUTTON

    def get_cart_items(self) -> list[CartItem]:
        """Return a CartItem component for every row in the cart."""
        return [CartItem(el) for el in self.find_all(self.cart_items_locator)]

    def click_checkout(self):
        """Click the checkout button."""
        self.click(self.checkout_button_locator)

    def click_continue_shopping(self):
        """Click the continue shopping button."""
        self.click(self.continue_shopping_button_locator)

    def remove_item_by_name(self, item_name: str):
        """Remove an item from the cart by its name."""
        for item in self.get_cart_items():
            if item.get_item_name() == item_name:
                item.click_remove()
                return
        raise ValueError(f"Cart item '{item_name}' not found")

    def empty_cart(self):
        """Remove all items from the cart."""
        for item in self.get_cart_items():
            item.click_remove()
