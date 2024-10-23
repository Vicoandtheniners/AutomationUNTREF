#Escribir un programa que dado el ingreso de un numero retorne si el mismo es primo o no.

numero = int(input("Ingrese un numero "))
es_primo= True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

if es_primo:
    print ( str(numero) + " es primo ")
else:
    print(str(numero) + " no es primo ")

    
#Escribir una función que dado el ingreso de 3 variables (a, b, c) retorne las raíces resultantes de una ecuación cuadrática.

import math

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    print(discriminante)

    if discriminante < 0:
        return "No hay raíces"
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return f"La raíz es: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Las raíces son: {raiz1} y {raiz2}"

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

resultado = calcular_raices(a, b, c)
print(resultado)



#El usuario se loguea al sitio como usuario standard user
#Ordenar los elementos por “price (low to high)”
#Verificar que los elementos estén ordenados

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_value("lohi")

prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
price_list = [float(price.text.replace('$', '')) for price in prices]
if price_list == sorted(price_list):
    print("Los productos están correctamente ordenados")
else:
    print("Los productos no están ordenados correctamente.")
driver.quit()




#El usuario se loguea al sitio como usuario standard user
#Incorporar al carrito todos los elementos
#Ir al carrito
#Verificar que todos los elementos están en el carrito
#Ir al checkout
#Ingresar nombre y clickear Continue
#Verificar que aparece el error “Error: Last Name is required”
#Ingresar un apellido y clickear Continue
#Verificar que aparece el error “Error: Postal Code is required”

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

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
assert len(cart_items) == len(items), "No todos los elementos están."

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys("Señora")
continue_button = driver.find_element(By.CLASS_NAME, "btn_primary")
continue_button.click()

error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
errortext = error_message.find_element(By.TAG_NAME, "h3")
assert errortext.text == "Error: Last Name is required", "El mensaje de error no es el mismo"

last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys("Vacalinda")
continue_button.click()

error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
errortext = error_message.find_element(By.TAG_NAME, "h3")
assert errortext.text == "Error: Postal Code is required", "El mensaje de error es incorrecto."

driver.quit()



#Caso 3


#El usuario se loguea al sitio como usuario standard user
#Agregar un elemento al carrito
#Ir al carrito
#Remover el artículo
#Verificar que el sitio no tiene artículos agregados
#Ir a Continue Shopping
#Agregar dos elementos
#Ir al carrito
#Verificar que los elementos existen
#Hacer el checkout
#Finalizar la compra
#Verificar que la compra fue realizada


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

    cart_item_list = driver.find_elements(By.CLASS_NAME, "cart_itemr")
    assert len(cart_item_list) == 0, "no se vacio"


    driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()

    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    add_buttons[0].click()
    add_buttons[1].click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, "No hay artículos"

    driver.find_element(By.CLASS_NAME, "checkout_button").click()

    driver.find_element(By.ID, "first-name").send_keys("Victoria")
    driver.find_element(By.ID, "last-name").send_keys("Saucedo")
    driver.find_element(By.ID, "postal-code").send_keys(1704)
    driver.find_element(By.CLASS_NAME, "btn_primary").click()
    driver.find_element(By.ID, "finish").click()

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in confirmation_message.text, "La compra no se realizo "
    driver.quit()


if __name__ == "__main__":
    test_cart_and_checkout()


#Caso 1 

#Hacer un get a berry/1
#Verificar que el size sea 20
#Verificar que el soildryness sea 15
#Verificar que en firmness, el name sea soft.

import requests

def testberryendpoint():
    url = "https://pokeapi.co/api/v2/berry/1"

    response = requests.get(url)

    assert response.status_code == 200, f"Error: {response.status_code}. No se pudo acceder al endpoint."

    berry_data = response.json()

    assert berry_data['size'] == 20, f"El tamaño esperado es 20, pero se recibió {berry_data['size']}."

    assert berry_data['soil_dryness'] == 15, f"La sequedad del suelo esperada es 15, pero se recibió {berry_data['soil_dryness']}."

    assert berry_data['firmness']['name'] == "soft", f" firmeza esperado es 'soft', pero se recibió '{berry_data['firmness']['name']}'."
    print('La prueba ha finalizado')
    
if __name__ == "__main__":
    testberryendpoint()



#Caso 2

#Hacer un get a berry/2
#Verificar que en firmness, el name sea super-hard
#Verificar que el size sea mayor al del punto anterior
#Verificar que el soildryness sea igual al del punto anterior

import requests

def test_berry_endpoints():
    url_1 = "https://pokeapi.co/api/v2/berry/1"
    response_1 = requests.get(url_1)
    assert response_1.status_code == 200, f"Error al acceder a berry/1: {response_1.status_code}."
    berry_1_data = response_1.json()

    url_2 = "https://pokeapi.co/api/v2/berry/2"
    response_2 = requests.get(url_2)
    assert response_2.status_code == 200, f"Error al acceder a berry/2: {response_2.status_code}."
    berry_2_data = response_2.json()

    assert berry_2_data['firmness']['name'] == "super-hard", f"El nombre de firmeza esperado es 'super-hard', pero se recibió '{berry_2_data['firmness']['name']}'."

    assert berry_2_data['size'] > berry_1_data['size'], f"El size esperado para berry/2 debe ser mayor que {berry_1_data['size']}, pero se recibió {berry_2_data['size']}."

    assert berry_2_data['soil_dryness'] == berry_1_data['soil_dryness'], f"El soil_dryness de berry/2 debe ser igual a {berry_1_data['soil_dryness']}, pero se recibió {berry_2_data['soil_dryness']}."
    print('La prueba ha finalizado')
    
    
if __name__ == "__main__":
    test_berry_endpoints()





#Caso 3

#Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/)
#Verificar que su experiencia base es mayor a 10 y menor a 1000
#Verificar que su tipo es “electric”


import requests

def test_pikachu_endpoint():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    
    response = requests.get(url)
    
    assert response.status_code == 200, f"Error: {response.status_code}. No se pudo acceder al endpoint."
    
    pikachu_data = response.json()
    
    base_experience = pikachu_data['base_experience']
    assert 10 < base_experience < 1000, f"La experiencia base de Pikachu debe ser mayor a 10 y menor a 1000, pero se recibió {base_experience}."
    
    types = [type_info['type']['name'] for type_info in pikachu_data['types']]
    assert "electric" in types, f"Pikachu debe ser de tipo 'electric', pero se encontró: {types}."
    print('La prueba ha finalizado')
    
    
if __name__ == "__main__":
    test_pikachu_endpoint()
