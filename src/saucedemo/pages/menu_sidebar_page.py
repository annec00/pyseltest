from selenium.webdriver.common.by import By

from src.common.base_page import BasePage


class MenuSidebarPage(BasePage):
    """The sliding sidebar panel opened from the header's burger button."""

    # Locators (all inside the sliding panel)
    CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")
    INVENTORY_LINK = (By.ID, "inventory_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def close_menu(self):
        self.click(self.CLOSE_BUTTON)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)
