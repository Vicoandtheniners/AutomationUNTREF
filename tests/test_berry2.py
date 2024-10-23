import requests
import unittest

class TestBerryAPI(unittest.TestCase):
    def test_berry_2(self):
        url_1 = "https://pokeapi.co/api/v2/berry/1"
        response_1 = requests.get(url_1)
        self.assertEqual(response_1.status_code, 200, f"Error al acceder a berry/1: {response_1.status_code}.")
        berry_1_data = response_1.json()

        url_2 = "https://pokeapi.co/api/v2/berry/2"
        response_2 = requests.get(url_2)
        self.assertEqual(response_2.status_code, 200, f"Error al acceder a berry/2: {response_2.status_code}.")
        berry_2_data = response_2.json()

        self.assertEqual(berry_2_data['firmness']['name'], "super-hard", 
                         f"El nombre de firmeza esperado es 'super-hard', pero se recibió '{berry_2_data['firmness']['name']}'.")

        self.assertGreater(berry_2_data['size'], berry_1_data['size'], 
                           f"El size esperado para berry/2 debe ser mayor que {berry_1_data['size']}, pero se recibió {berry_2_data['size']}.")

        self.assertEqual(berry_2_data['soil_dryness'], berry_1_data['soil_dryness'], 
                         f"El soil_dryness de berry/2 debe ser igual a {berry_1_data['soil_dryness']}, pero se recibió {berry_2_data['soil_dryness']}.")

if __name__ == '__main__':
    unittest.main()
