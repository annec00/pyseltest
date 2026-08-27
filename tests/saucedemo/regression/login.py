from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options




def test_login_logout():


    chrome_options = Options()

    prefs = {
        # "credentials_enable_service": False,
        # "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }


    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://www.saucedemo.com/")

    sleep(2)

    # username_input = driver.find_element("id", "user-name")
    username_input = driver.find_element(by=By.ID, value="user-name")
    password_input = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    sleep(10)


    page_title = driver.find_element(by=By.CLASS_NAME, value="title")
    assert page_title.text == "Products"

    menu_button = driver.find_element(by=By.ID, value="react-burger-menu-btn")
    menu_button.click()

    sleep(2)
    logout_link = driver.find_element(by=By.ID, value="logout_sidebar_link")
    logout_link.click()

    sleep(10)

    driver.quit()
