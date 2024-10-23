import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AutomationTP import calcular_raices  

class TestCalcularRaices(unittest.TestCase):
    
    def test_raices_dos_soluciones(self):
        self.assertEqual(calcular_raices(1, -3, 2), "Las raíces son: 2.0 y 1.0")
    
    def test_raices_una_solucion(self):
        self.assertEqual(calcular_raices(1, 2, 1), "La raíz es: -1.0")
    
    def test_raices_no_soluciones(self):
        self.assertEqual(calcular_raices(1, 0, 1), "No hay raíces")

if __name__ == '__main__':
    unittest.main()
