from selenium.webdriver.common.by import By

from src.common.base_page import BasePage
from src.saucedemo.components.inventory_item import InventoryItem


class HomePage(BasePage):

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self, timeout=10):
        """Wait for the home page to load by checking the visibility of the page title."""
        self.wait_for_visible(self.PAGE_TITLE)

    def get_page_title(self):
        """Get the title of the home page."""
        return self.get_text(self.PAGE_TITLE)

    def get_inventory_items(self) -> list[InventoryItem]:
        """Return an InventoryItem component for every product card on the page."""
        return [InventoryItem(el) for el in self.find_all(self.INVENTORY_ITEM)]

    def get_inventory_item(self, name: str) -> InventoryItem:
        """Return the InventoryItem component whose product name matches `name`."""
        for item in self.get_inventory_items():
            if item.get_name() == name:
                return item
        raise ValueError(f"Inventory item '{name}' not found")
