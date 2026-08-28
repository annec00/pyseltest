import pytest

from src.common.driver_factory import DriverFactory

def pytest_addoption(parser):
    """Allows pulling browser configurations directly from the terminal."""
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests on"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

@pytest.fixture(scope="function")
def driver(request):
    """Fixture to initialize the WebDriver based on the specified browser."""
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser_name, headless=headless)
    yield driver
    driver.quit()