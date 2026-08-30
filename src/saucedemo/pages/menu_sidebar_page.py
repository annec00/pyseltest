from selenium.webdriver.common.by import By

from src.common.base_page import BasePage


class MenuSidebarPage(BasePage):

    # Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)
