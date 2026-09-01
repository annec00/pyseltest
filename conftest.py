import pytest

from config.restful_booker_config import BASE_URL
from src.common.driver_factory import DriverFactory
from src.restful_booker.booking_service import BookingService
from src.saucedemo.pages.cart_page import CartPage
from src.saucedemo.pages.header_page import HeaderPage
from src.saucedemo.pages.login_page import LoginPage


def pytest_addoption(parser):
    """Allows pulling browser configurations directly from the terminal."""
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser to run tests on",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode",
    )


# For UI Tests
@pytest.fixture(scope="function")
def driver(request):
    """Fixture to initialize the WebDriver based on the specified browser."""
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser_name, headless=headless)
    yield driver
    driver.quit()


# Log in as whichever user the test asks for; log out afterwards.
@pytest.fixture(scope="function")
def login_as(driver):
    """Yield a helper: call `login_as("problem_user")` in the test to log in as that user."""
    state = {"logged_in": False}

    def _login(username, password="secret_sauce"):
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.wait_for_page_load()
        login_page.login(username, password)
        state["logged_in"] = True

    yield _login

    if state["logged_in"]:
        HeaderPage(driver).logout()


# Helper to clear the cart; call it in the test after logging in.
@pytest.fixture(scope="function")
def empty_cart(driver):
    """Return a helper that navigates to the cart and removes all items."""

    def _clear():
        HeaderPage(driver).click_cart_icon()
        cart_page = CartPage(driver)
        cart_page.empty_cart()
        cart_page.click_continue_shopping()  # back to the products page

    return _clear


# For API Tests
@pytest.fixture(scope="session")
def booking_service():
    """Fixture to provide a BookingService instance for API tests."""
    return BookingService(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(booking_service):
    """Fixture to provide an authentication token for tests."""
    return booking_service.authenticate("admin", "password123")


@pytest.fixture(scope="function")
def booking_id(booking_service):
    """Fixture to provide the booking_id for tests."""
    # Create a booking to ensure there's at least one booking available for tests
    booking_payload = {
        "firstname": "PyTestAPI",
        "lastname": "AC",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-10"},
        "additionalneeds": "Breakfast",
    }
    response = booking_service.create_booking(booking_payload)
    if response.status_code == 200:
        booking_id = response.json().get("bookingid")
        return booking_id
    else:
        pytest.skip("No booking ID available for tests.")
