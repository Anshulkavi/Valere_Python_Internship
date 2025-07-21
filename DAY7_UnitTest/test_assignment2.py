import unittest
from assignment2 import Prime

class TestPrime(unittest.TestCase):

    def test_equal_to_one_or_negative(self):
        self.assertEqual(Prime(1), '1 is not a prime number')
        self.assertEqual(Prime(-1), '-1 is not a prime number')
        self.assertEqual(Prime(0), '0 is not a prime number')

    def test_equal_to_two(self):
        self.assertEqual(Prime(2), '2 is a prime number')

    def test_even_number_greater_than_two(self):
        self.assertEqual(Prime(10), '10 is not a prime number')

    def test_odd_non_prime(self):
        self.assertEqual(Prime(9), '9 is not a prime number')

    def test_odd_prime(self):
        self.assertEqual(Prime(13), '13 is a prime number') 

if __name__ == '__main__':
    unittest.main()       