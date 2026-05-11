import unittest
from string_calculator import sumar

class TestStringCalculator(unittest.TestCase):
    def test_cadena_vacia_devuelve_cero(self):
        self.assertEqual(sumar(""), 0)

    def test_un_numero_devuelve_el_mismo_numero(self):
        self.assertEqual(sumar("5"), 5)

    def test_un_numero_devuelve_el_mismo_numero(self):
        self.assertEqual(sumar("4"), 4)

    def test_dos_numeros_devuelve_la_suma(self):
        self.assertEqual(sumar("1,2"), 3)

    def test_dos_numeros_devuelve_la_suma(self):
        self.assertEqual(sumar("5,6"), 11)

if __name__ == '__main__':
    unittest.main()
