from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.cart1 = StudentReportCard("name1", 1)

    def test_correct_initialization(self):
        self.assertEqual("name1", self.cart1.student_name)
        self.assertEqual(1, self.cart1.school_year)
        self.assertEqual({}, self.cart1.grades_by_subject)

    def test_student_name_raises_val_error_for_empty_name_string(self):
        with self.assertRaises(ValueError) as ve:
            self.cart1.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("", 1)
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_raises_val_error_for_invalid_school_year(self):
        # below limit
        with self.assertRaises(ValueError) as ve:
            self.cart1.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("student", -1)
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

        # above limit
        with self.assertRaises(ValueError) as ve:
            self.cart1.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("student", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_sets_school_year_correctly_at_limits(self):
        cart2 = StudentReportCard("student", 1)
        cart3 = StudentReportCard("student", 12)
        self.assertEqual(1, cart2.school_year)
        self.assertEqual(12, cart3.school_year)

    def test_add_grade_adds_subject_and_grades_correctly(self):
        # add subject to empty dict
        result1 = self.cart1.add_grade("Math", 4.5)
        self.assertEqual({"Math": [4.5]}, self.cart1.grades_by_subject)
        self.assertEqual(None, result1)

        # add one more subject
        result2 = self.cart1.add_grade("CompSci", 6.0)
        self.assertEqual({"Math": [4.5], "CompSci": [6.0]}, self.cart1.grades_by_subject)
        self.assertEqual(None, result2)

        # add new grade to existing subject
        result3 = self.cart1.add_grade("CompSci", 6.0)
        self.assertEqual({"Math": [4.5], "CompSci": [6.0, 6.0]}, self.cart1.grades_by_subject)
        self.assertEqual(None, result3)

        # add one more grade to existing subject
        result4 = self.cart1.add_grade("Math", 5.0)
        self.assertEqual({"Math": [4.5, 5.0], "CompSci": [6.0, 6.0]}, self.cart1.grades_by_subject)
        self.assertEqual(None, result4)

    def test_ave_grade_by_subj_gives_correct_info(self):
        # empty subject dict
        result1 = self.cart1.average_grade_by_subject()
        self.assertEqual("", result1)

        # one subject
        self.cart1.grades_by_subject = {"Math": [5.0]}
        result = self.cart1.average_grade_by_subject()
        expected = "Math: 5.00"
        self.assertEqual(expected, result)

        # non-empty subject dict
        self.cart1.grades_by_subject = {
            "Math": [5.0, 5.0],
            "CompSci": [6.0, 0.0],
            "Physics": [5.5]}
        result2 = self.cart1.average_grade_by_subject()
        expected = "Math: 5.00\nCompSci: 3.00\nPhysics: 5.50"
        self.assertEqual(expected, result2)

        # non-empty subject dict with 0 grades
        self.cart1.grades_by_subject = {
            "Math": [0, 0],
            "CompSci": [0],
            "Physics": [0]}
        self.assertEqual("Math: 0.00\nCompSci: 0.00\nPhysics: 0.00", self.cart1.average_grade_by_subject())

    def test_ave_grade_for_all_gives_correct_info(self):
        # empty subject dict
        with self.assertRaises(ZeroDivisionError) as zde:
            self.cart1.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(zde.exception))

        # non-empty subject dict, no grades
        self.cart1.grades_by_subject = {
            "Math": [],
            "CompSci": [],
            "Physics": []}
        with self.assertRaises(ZeroDivisionError) as zde:
            self.cart1.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(zde.exception))

        # one-non-empty subject dict
        self.cart1.grades_by_subject = {
            "Math": [],
            "CompSci": [6.0, 2.0],
            "Physics": []}
        result = self.cart1.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.00", result)

        # non-empty subject dict and present grades
        self.cart1.grades_by_subject = {
            "Math": [5.0, 5.0],
            "CompSci": [6.0, 6.0],
            "Physics": [8.0]}
        result1 = self.cart1.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 6.00", result1)

        # non-empty subject dict and 0 grades
        self.cart1.grades_by_subject = {
            "Math": [0, 0],
            "CompSci": [0],
            "Physics": [0]}
        result2 = self.cart1.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 0.00", result2)

    def test_repr_returns_correct_info(self):
        # empty subject list
        with self.assertRaises(ZeroDivisionError) as zde:
            repr(self.cart1)
        self.assertEqual("division by zero", str(zde.exception))

        # non-empty subject dict, no grades
        self.cart1.grades_by_subject = {
            "Math": [],
            "CompSci": [],
            "Physics": []}
        with self.assertRaises(ZeroDivisionError) as zde:
            repr(self.cart1)
        self.assertEqual("division by zero", str(zde.exception))

        # non-empty
        self.cart1.grades_by_subject = {
            "Math": [5.0, 5.0],
            "CompSci": [6.0, 6.0],
            "Physics": [8.0]}

        result1 = repr(self.cart1)
        expected = "Name: name1\n" \
                   "Year: 1\n" \
                   "----------\n" \
                   "Math: 5.00\nCompSci: 6.00\nPhysics: 8.00\n" \
                   "----------\n" \
                   "Average Grade: 6.00"
        self.assertEqual(expected, result1)


if __name__ == "__main__":
    main()
