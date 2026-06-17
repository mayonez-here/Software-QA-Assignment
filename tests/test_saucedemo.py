from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver():
    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install())
    )
    driver.maximize_window()
    return driver


def test_valid_login():
    driver = get_driver()

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

    driver.quit()


def test_add_item_and_checkout():
    driver = get_driver()

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    success_message = driver.find_element(
        By.CLASS_NAME,
        "complete-header"
    ).text

    assert "Thank you" in success_message

    driver.quit()

# I selected three critical user journeys required in the assignment. The first verifies successful authentication, the second verifies the core purchasing workflow from login to order completion, and the third validates proper error handling for a locked-out account. Together they cover both positive and negative scenarios and the most important functionality of the application.
def test_locked_out_user():
    driver = get_driver()

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.TAG_NAME, "h3").text

    assert "locked out" in error_message.lower()

    driver.quit()