import unittest
from calculadora import Calculadora

class TestesCalculadora(unittest.TestCase):
    def test_soma(self):
        calc = Calculadora(10, 5)
        self.assertEqual(calc.somar(), 15)

    def test_divisao(self):
        calc = Calculadora(10, 2)
        self.assertEqual(calc.dividir(), 5.0)
    
    def test_subtracao(self):
        calc = Calculadora (20, 10)
        self.assertEqual(calc.subtrair(), 10)
    
    def test_multiplicacao(self):
        calc = Calculadora (5, 5)
        self.assertEqual(calc.multiplicar(), 25)
    
    def test_divisao_por_zero(self):
        calc = Calculadora(10, 0)
        self.assertEqual(calc.dividir(), "Não é possível dividir por zero.")

if __name__ == '__main__':
    unittest.main()