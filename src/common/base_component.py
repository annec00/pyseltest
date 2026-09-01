from selenium.webdriver.remote.webelement import WebElement


class BaseComponent:
    """Base class for component objects.

    A component object wraps a single root WebElement (a repeated chunk of UI
    such as a card, row, or modal) and scopes all lookups to that root, so the
    same component can be reused for every instance on the page.
    """

    def __init__(self, root: WebElement):
        self.root = root

    def find(self, locator: tuple):
        """Find a descendant element relative to this component's root."""
        return self.root.find_element(*locator)

    def find_all(self, locator: tuple):
        """Find all descendant elements relative to this component's root."""
        return self.root.find_elements(*locator)

    def get_text(self, locator: tuple) -> str:
        """Get the text of a descendant element specified by the locator."""
        return self.find(locator).text

    def click(self, locator: tuple):
        """Click on a descendant element specified by the locator."""
        self.find(locator).click()
