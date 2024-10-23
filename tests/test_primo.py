import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from AutomationTP import es_primo  # Importa la función es_primo desde AutomationTP.py


import unittest
from AutomationTP import es_primo  

class TestEsPrimo(unittest.TestCase):
    def test_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        
    def test_no_primos(self):
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(9))
        self.assertFalse(es_primo(10))

if __name__ == '__main__':
    unittest.main()
