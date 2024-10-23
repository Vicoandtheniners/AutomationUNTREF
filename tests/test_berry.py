import requests
import unittest

class TestBerryAPI(unittest.TestCase):
    def test_berry_1(self):
        url = "https://pokeapi.co/api/v2/berry/1"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200, f"Error: {response.status_code}. No se pudo acceder al endpoint.")

        berry_data = response.json()

        self.assertEqual(berry_data['size'], 20, f"El tamaño esperado es 20, pero se recibió {berry_data['size']}.")

        self.assertEqual(berry_data['soil_dryness'], 15, f"La sequedad del suelo esperada es 15, pero se recibió {berry_data['soil_dryness']}.")

        self.assertEqual(berry_data['firmness']['name'], "soft", f"Firmeza esperado es 'soft', pero se recibió '{berry_data['firmness']['name']}'.")

        print('La prueba ha finalizado')

if __name__ == '__main__':
    unittest.main()
