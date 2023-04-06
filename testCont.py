import unittest
from contadorDePalabras import contadorDePalabras

class testContadorDePalabras(unittest.TestCase):
    def test_1 (self):
        resultado = contadorDePalabras("hola como hola en")
        self.assertEqual(resultado,{ 'hola': 2, 'como' : 1, 'en' : 1})

if __name__=="__main__":
    unittest.main()