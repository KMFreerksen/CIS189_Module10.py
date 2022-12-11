import unittest
from class_definitions import Student_Class as S

class StudentTest  (unittest.TestCase):
    def setUp(self):
        self.Student = S.Student('White', 'Walter', 'Chemistry', 4.00)

    def tearDown(self):
        del self.Student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.Student.first_name,'Walter')
        self.assertEqual(self.Student.last_name,'White')
        self.assertEqual(self.Student.major, 'Chemistry')

    def test_object_created_all_attributes(self):
        student = S.Student('Pinkman','Jesse','HiSet')
        assert student.last_name == 'Pinkman'
        assert student.first_name == 'Jesse'
        assert student.major == 'HiSet'
        assert student.gpa == 0.00

    def test_student_str(self):
        self.assertEqual(str(self.Student), 'White, Walter has major Chemistry with gpa: 4.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            n = S.Student('4444', 'White','Chemistry', 4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            n = S.Student('Walter','4444', 'Chemistry', 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            n = S.Student('Walter','White', '4444', 4.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            n = S.Student('Walter','White','Chemistry',40)
