from src.saucedemo.pages.cart_page import CartPage
from src.saucedemo.pages.checkout_step_one_page import CheckoutStepOnePage
from src.saucedemo.pages.checkout_step_two_page import CheckoutStepTwoPage
from src.saucedemo.pages.header_page import HeaderPage
from src.saucedemo.pages.home_page import HomePage


def test_checkout_an_item(driver, login_as, empty_cart):
    """Test the checkout process for a single item on the SauceDemo website."""
    # Log in as a standard user
    login_as("standard_user")
    empty_cart()  # Ensure the cart is empty before starting the test

    # Add an item to the cart
    home_page = HomePage(driver)
    home_page.click_add_to_cart_by_name("Sauce Labs Backpack")

    # Proceed to checkout
    header = HeaderPage(driver)
    header.click_cart_icon()
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Fill in checkout information
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_one_page.enter_first_name("John")
    checkout_step_one_page.enter_last_name("Doe")
    checkout_step_one_page.enter_zip_code("12345")
    checkout_step_one_page.click_continue()

    # Verify that the item is present on the checkout overview page
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    cart_items = checkout_step_two_page.get_cart_items()
    assert len(cart_items) == 1, "There should be one item in the cart."
    assert (
        cart_items[0].get_item_name() == "Sauce Labs Backpack"
    ), "The item in the cart should be 'Sauce Labs Backpack'."

    # Compute the expected total based on item price and tax
    item_total = float(cart_items[0].get_item_price().replace("$", ""))
    item_tax = item_total * 0.08
    # round total to 2 decimal places
    expected_total = round(item_total + item_tax, 2)

    # Verify the total item price displayed
    displayed_item_total = float(
        checkout_step_two_page.get_price_total_item_total().replace("Item total: $", "")
    )
    assert (
        displayed_item_total == item_total
    ), f"Expected item total: ${item_total}, but got: ${displayed_item_total}"

    # Verify the tax displayed
    displayed_tax = float(checkout_step_two_page.get_price_tax().replace("Tax: $", ""))
    assert displayed_tax == round(
        item_tax, 2
    ), f"Expected tax: ${round(item_tax, 2)}, but got: ${displayed_tax}"

    # Verify the total price displayed
    displayed_total = float(
        checkout_step_two_page.get_price_total().replace("Total: $", "")
    )
    assert (
        displayed_total == expected_total
    ), f"Expected total: ${expected_total}, but got: ${displayed_total}"

    # Complete the checkout process
    checkout_step_two_page.click_finish()

    # Verify that the checkout complete page is displayed
    assert (
        checkout_step_two_page.get_page_title() == "Checkout: Complete!"
    ), "Checkout complete page title does not match."
