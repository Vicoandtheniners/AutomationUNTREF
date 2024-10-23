import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestOrdenamientoProductos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def test_ordenamiento_productos(self):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")

        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        price_list = [float(price.text.replace('$', '')) for price in prices]

        self.assertEqual(price_list, sorted(price_list), "Los productos no están ordenados correctamente.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
