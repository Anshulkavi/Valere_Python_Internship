# test file
import unittest
from Bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        print("Setting up...")
        self.acc = BankAccount("Anshul", 1000)

    def tearDown(self):
        print("Tearing down...")

    def test_deposit(self):
        self.acc.deposit(500)
        self.assertEqual(self.acc.get_balance(),1500)

    def test_withdraw(self):
        self.acc.withdraw(400)
        self.assertEqual(self.acc.get_balance(),600)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(2000)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-100) 

    def test_balance(self):
        self.assertTrue(self.acc.get_balance() >= 0)

if __name__ == '__main__':
    unittest.main()                               