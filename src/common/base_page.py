from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        """Open the specified URL in the browser."""
        self.driver.get(url)

    def find(self, locator: tuple):
        """Find an element on the page using the specified locator."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator: tuple):
        """Find all elements on the page using the specified locator."""
        return self.driver.find_elements(*locator)

    def wait_for_visible(self, locator: tuple):
        """Wait for an element to be visible on the page."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        """Click on an element specified by the locator."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: tuple, text: str):
        """Type text into an input field specified by the locator."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get the text of an element specified by the locator."""
        element = self.find(locator)
        return element.text

    def is_element_displayed(self, locator: tuple) -> bool:
        """Check if an element specified by the locator is displayed."""
        try:
            element = self.find(locator)
            return element.is_displayed()
        except Exception:
            return False
