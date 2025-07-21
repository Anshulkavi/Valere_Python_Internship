import unittest
from unittest.mock import patch
import io

from assignment3 import students, add_students, search_student, update_marks, delete_students

class SimpleStudentTests(unittest.TestCase):

    def test_add_students(self):
        students.clear()  # Clear existing data for clean test
        with patch('builtins.input', side_effect=[
            'Ravi', '2', 'Math', '88', 'Science', '92'
        ]), patch('sys.stdout', new=io.StringIO()) as fake_out:
            add_students()
            self.assertIn('Ravi', students)
            self.assertEqual(students['Ravi']['Math'], 88)
            self.assertIn("Student added successfully", fake_out.getvalue())

    def test_search_existing_student(self):
        students.clear()
        students['Aman'] = {'Math': 90, 'English': 85}
        with patch('builtins.input', return_value='Aman'), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            search_student()
            output = fake_out.getvalue()
            self.assertIn("Aman's Marks", output)
            self.assertIn("Math: 90", output)

    def test_update_marks(self):
        students.clear()
        students['Aman'] = {'Math': 90, 'English': 85}
        with patch('builtins.input', side_effect=['Aman', 'Math', '95']), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            update_marks()
            self.assertEqual(students['Aman']['Math'], 95)
            self.assertIn("Marks updated", fake_out.getvalue())

    def test_delete_student(self):
        students.clear()
        students['Aman'] = {'Math': 90, 'English': 85}
        with patch('builtins.input', side_effect=['Aman', 'y']), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            delete_students()
            self.assertNotIn('Aman', students)
            self.assertIn("Student deleted", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
