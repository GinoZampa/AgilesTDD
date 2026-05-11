import unittest
from string_calculator import sumar

class TestStringCalculator(unittest.TestCase):
    def test_cadena_vacia_devuelve_cero(self):
        self.assertEqual(sumar(""), 0)

if __name__ == '__main__':
    unittest.main()
