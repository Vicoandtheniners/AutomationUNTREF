import requests
import unittest

class TestPikachuAPI(unittest.TestCase):
    def test_pikachu(self):
        url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        pikachu_data = response.json()
        base_experience = pikachu_data['base_experience']
        self.assertGreater(base_experience, 10)
        self.assertLess(base_experience, 1000)

if __name__ == '__main__':
    unittest.main()
