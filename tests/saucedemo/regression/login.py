from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_login_logout(driver):

    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 2);
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))

    username_input = driver.find_element(by=By.ID, value="user-name")
    password_input = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    menu_button = wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    page_title = driver.find_element(by=By.CLASS_NAME, value="title")

    assert page_title.text == "Products"

    print("Login successful. Page title is:", page_title.text)
    print("Waiting for 2 seconds before logging out...")
    sleep(2)
    wait.until(EC.element_to_be_clickable((menu_button))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

