import unittest
import requests

class TestPikachuAPI(unittest.TestCase):
    
    def test_pikachu(self):
        url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
        response = requests.get(url)
        
        self.assertEqual(response.status_code, 200, f"Error: {response.status_code}. No se pudo acceder al endpoint.")
        
        pikachu_data = response.json()
        
 
        base_experience = pikachu_data['base_experience']
        self.assertTrue(10 < base_experience < 1000, f"La experiencia base de Pikachu debe ser mayor a 10 y menor a 1000, pero se recibió {base_experience}.")
        
   
        types = [type_info['type']['name'] for type_info in pikachu_data['types']]
        self.assertIn("electric", types, f"Pikachu debe ser de tipo 'electric', pero se encontró: {types}.")

if __name__ == "__main__":
    unittest.main()
