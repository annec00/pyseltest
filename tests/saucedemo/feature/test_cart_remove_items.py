from src.saucedemo.pages.cart_page import CartPage
from src.saucedemo.pages.header_page import HeaderPage
from src.saucedemo.pages.home_page import HomePage


def test_cart_remove_items(driver, login_as, empty_cart):
    # Log in as a standard user
    login_as("standard_user")
    empty_cart()  # Ensure the cart is empty before starting the test

    # Add items to the cart
    home_page = HomePage(driver)
    home_page.click_add_to_cart_by_name("Sauce Labs Backpack")
    home_page.click_add_to_cart_by_name("Sauce Labs Bike Light")

    # Verify that the cart is empty
    header = HeaderPage(driver)
    header.click_cart_icon()
    cart_page = CartPage(driver)
    cart_page.click_remove_item_by_name("Sauce Labs Backpack")

    # Verify that the item has been removed from the cart, and item is no longer present
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 1
    assert cart_items[0].get_item_name() != "Sauce Labs Backpack"

    cart_page.click_remove_item_by_name("Sauce Labs Bike Light")
    # Verify that there is no more remaining item

    assert len(cart_page.get_cart_items()) == 0
