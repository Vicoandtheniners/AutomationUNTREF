from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart_and_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    add_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_button.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.CLASS_NAME, "cart_button").click()

    cart_item_list = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_item_list) == 0, "El carrito no está vacío."

    driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()

    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    add_buttons[0].click()
    add_buttons[1].click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, "No hay artículos en el carrito."

    driver.find_element(By.CLASS_NAME, "checkout_button").click()

    driver.find_element(By.ID, "first-name").send_keys("Victoria")
    driver.find_element(By.ID, "last-name").send_keys("Saucedo")
    driver.find_element(By.ID, "postal-code").send_keys(1704)
    driver.find_element(By.CLASS_NAME, "btn_primary").click()
    driver.find_element(By.ID, "finish").click()


    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in confirmation_message.text, "La compra no se realizó."

    driver.quit()

if __name__ == "__main__":
    test_cart_and_checkout()
