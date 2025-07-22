'''
Python's unittest Module
Python comes with a built-in module called unittest
that supports test automation, setup/teardown, and
more.
'''

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == '__main__':
    unittest.main()

'''
Key unittest Methods
Method	              Description
assertEqual(a, b)	   Check a == b
assertNotEqual(a, b)   Check a != b
assertTrue(x)	       Check bool(x) is True
assertFalse(x)	       Check bool(x) is False
assertIsNone(x)	       Check x is None
assertRaises(Error)	   Check exception is raised
'''

