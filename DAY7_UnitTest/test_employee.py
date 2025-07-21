import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Alice", 101, 50000)

    def test_initial_salary(self):
        self.assertEqual(self.emp.get_salary(),50000)

    def test_bonus_addition(self):
        self.emp.set_bonus(5000)
        
        with self.assertRaises(ValueError):
            self.emp.set_bonus(-1000) # # Negative bonus should raise ValueError

    def test_negative_bonus_raises_error(self):
        self.emp.set_bonus(2000)
        expected = "Alice (ID: 101) - Salary: 52000"
        self.assertEqual(str(self.emp), expected)


if __name__ == '__main__':
    unittest.main()