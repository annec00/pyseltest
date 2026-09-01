from selenium.webdriver.common.by import By

from src.common.base_page import BasePage
from src.saucedemo.pages.menu_sidebar_page import MenuSidebarPage


class HeaderPage(BasePage):
    """Represents the header section of the page."""

    # Locators
    LOGO = (By.CLASS_NAME, "app_logo")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)
        self.logo_locator = self.LOGO
        self.menu_button_locator = self.MENU_BUTTON

    def is_logo_displayed(self) -> bool:
        """Check if the logo is displayed."""
        return self.is_element_displayed(self.logo_locator)

    def open_menu(self):
        """Open the burger menu; the sidebar slides in from the left."""
        self.click(self.menu_button_locator)

    def click_cart_icon(self):
        """Click the cart icon in the header to navigate to the cart page."""
        self.click(self.CART_ICON)

    def get_cart_item_count(self) -> int:
        """Get the number of items in the cart, as displayed in the cart icon badge."""
        try:
            cart_badge = self.find(self.CART_BADGE)
            return int(cart_badge.text)
        except Exception:
            return 0

    def logout(self):
        """Open the burger menu and click Logout in the sidebar."""
        self.open_menu()
        MenuSidebarPage(self.driver).click_logout()
