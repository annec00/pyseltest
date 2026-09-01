from selenium.webdriver.common.by import By

from src.common.base_component import BaseComponent


class InventoryItem(BaseComponent):
    """Component object for a single product card in the SauceDemo inventory list."""

    # Locators (all resolved relative to the card's root element)
    NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    DESC = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    TITLE_LINK = (By.CSS_SELECTOR, ".inventory_item_label a")
    IMG_LINK = (By.CSS_SELECTOR, ".inventory_item_img a")
    # The action button toggles between "Add to cart" and "Remove"; its
    # data-test attribute changes with it, but btn_inventory is stable.
    ACTION_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")

    def get_name(self) -> str:
        return self.get_text(self.NAME)

    def get_description(self) -> str:
        return self.get_text(self.DESC)

    def get_price(self) -> str:
        return self.get_text(self.PRICE)

    def get_price_value(self) -> float:
        """Get the price as a float, stripping the currency symbol."""
        return float(self.get_price().replace("$", "").strip())

    def is_in_cart(self) -> bool:
        return self.get_text(self.ACTION_BUTTON).strip().lower() == "remove"

    def add_to_cart(self):
        if not self.is_in_cart():
            self.find(self.ACTION_BUTTON).click()

    def remove_from_cart(self):
        if self.is_in_cart():
            self.find(self.ACTION_BUTTON).click()

    def open_details(self):
        """Open this item's detail page by clicking its title link."""
        self.find(self.TITLE_LINK).click()
