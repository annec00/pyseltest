from src.saucedemo.pages.home_page import HomePage
from src.saucedemo.pages.login_page import LoginPage
from src.saucedemo.pages.menu_sidebar_page import MenuSidebarPage


def test_login_logout(driver):
    menu_sidebar = MenuSidebarPage(driver)
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.open_page()
    login_page.wait_for_page_load()

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    home_page.wait_for_page_load()

    assert home_page.get_page_title() == "Products"

    menu_sidebar.open_menu()
    menu_sidebar.click_logout()

    login_page.wait_for_page_load()
    assert login_page.driver.current_url == login_page.url
