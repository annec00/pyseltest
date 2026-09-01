from selenium.webdriver.common.by import By

from src.common.base_component import BaseComponent


class CartItem(BaseComponent):
    """Represents a single item in the cart page."""

    # Locators
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")

    def get_item_name(self):
        """Return the name of the item."""
        return self.get_text(self.ITEM_NAME)

    def get_item_description(self):
        """Return the description of the item."""
        return self.get_text(self.ITEM_DESC)

    def get_item_price(self):
        """Return the price of the item."""
        return self.get_text(self.ITEM_PRICE)

    def click_remove(self):
        """Click the remove button for this item."""
        self.click(self.REMOVE_BUTTON)
