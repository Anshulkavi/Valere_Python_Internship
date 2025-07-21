import unittest
from assignment1 import calculate

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(10,5,'+'), 15)

    def test_substraction(self):
        self.assertEqual(calculate(10,5,'-'), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(10,5,'*'),50)

    def test_division(self):
        self.assertEqual(calculate(10,5,'/'),2)    

    def  test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10,0,'/')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(10,5,'%')        


if __name__ == '__main__':
    unittest.main()        