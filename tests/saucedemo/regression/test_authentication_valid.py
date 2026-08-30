from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.saucedemo.components.menu_sidebar import MenuSidebar
from src.saucedemo.pages.home_page import HomePage
from src.saucedemo.pages.login_page import LoginPage



def test_login_logout(driver):
    menu_sidebar = MenuSidebar(driver)

    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.load()


    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    home_page.wait_for_page_to_load()

    assert home_page.get_page_title() == "Products"

    print("Login successful. Page title is:", home_page.get_page_title())
    print("Waiting for 2 seconds before logging out...")
    sleep(2)

    menu_sidebar.open_menu()
    menu_sidebar.click_logout()

    login_page.load()
    assert login_page.driver.current_url == login_page.url


