import requests
import unittest

class TestBerryAPI(unittest.TestCase):
    def test_berry_1(self):
        url = "https://pokeapi.co/api/v2/berry/1"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        berry_data = response.json()
        self.assertEqual(berry_data['size'], 20)

if __name__ == '__main__':
    unittest.main()
