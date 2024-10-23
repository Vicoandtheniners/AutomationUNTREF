import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCarritoCompra(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def test_carrito_y_checkout(self):
        driver = self.driver
        
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        items = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for item in items:
            item.click()

        cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), len(items), "No todos los elementos están en el carrito.")

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        first_name_input = driver.find_element(By.ID, "first-name")
        first_name_input.send_keys("Señora")
        continue_button = driver.find_element(By.CLASS_NAME, "btn_primary")
        continue_button.click()

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        errortext = error_message.find_element(By.TAG_NAME, "h3")
        self.assertEqual(errortext.text, "Error: Last Name is required", "El mensaje de error no es el mismo.")

        last_name_input = driver.find_element(By.ID, "last-name")
        last_name_input.send_keys("Vacalinda")
        continue_button.click()

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        errortext = error_message.find_element(By.TAG_NAME, "h3")
        self.assertEqual(errortext.text, "Error: Postal Code is required", "El mensaje de error es incorrecto.")

        print('La prueba ha finalizado')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
