from selenium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(browser_name: str, headless: bool = False):
        """
        Get a Selenium WebDriver instance based on the specified browser name.
        Options: "chrome", "firefox"
        """
        browser_name = browser_name.lower().strip()

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            prefs = {
                "profile.password_manager_leak_detection": False,
            }
            options.add_experimental_option("prefs", prefs)

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("window-size=1920,1080")

            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            return driver

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            options.set_preference("profile.password_manager_leak_detection", False)
            if headless:
                options.add_argument("-headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")

            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            return driver

        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}. Supported browsers are: chrome, firefox."
            )
