from src.saucedemo.pages.header_page import HeaderPage
from src.saucedemo.pages.home_page import HomePage
from src.saucedemo.pages.login_page import LoginPage


def test_login_logout(driver):
    header = HeaderPage(driver)
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.open_page()
    login_page.wait_for_page_load()

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    home_page.wait_for_page_load()

    assert home_page.get_page_title() == "Products"

    header.logout()

    login_page.wait_for_page_load()
    assert login_page.driver.current_url == login_page.url
