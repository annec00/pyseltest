from src.saucedemo.pages.header_page import HeaderPage
from src.saucedemo.pages.home_page import HomePage


def test_cart_add_items(driver, login_as, empty_cart):
    """Test adding items to the cart on the SauceDemo home page."""
    login_as("standard_user")
    empty_cart()  # Ensure the cart is empty before starting the test

    home_page = HomePage(driver)
    home_page.wait_for_page_load()

    # Add the first two items to the cart
    inventory_items = home_page.get_inventory_items()
    for item in inventory_items[:2]:
        item.add_to_cart()
        assert item.is_in_cart(), f"Item '{item.get_name()}' should be in the cart."

    # Verify that the cart badge shows 2 items
    header_page = HeaderPage(driver)
    assert header_page.get_cart_item_count() == 2, "Cart badge should show 2 items."
