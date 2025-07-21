import unittest
from Product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        print("\nSetting up...")
        self.prod = Product("Apple", 60, 12)

    def tearDown(self):
        print("Tearing down...")

    def test_update_stock(self):
        self.prod.update_stock(25)  # quantity becomes 37
        self.assertEqual(self.prod.get_total_value(), 2220)  # 60 * 37

    def test_purchase(self):
        self.prod.purchase(5) # quantity = 7*
        self.assertEqual(self.prod.get_total_value(),420) # 60 * 7

    def test_purchase_insufficient_stock(self):
        with self.assertRaises(ValueError):
            self.prod.purchase(50)

    def test_invalid_purchase_negative(self):
        with self.assertRaises(ValueError):
            self.prod.purchase(-100)

    def test_invalid_update_stock(self):
        with self.assertRaises(ValueError):
            self.prod.update_stock(-20)        

if __name__ == '__main__':
    unittest.main()