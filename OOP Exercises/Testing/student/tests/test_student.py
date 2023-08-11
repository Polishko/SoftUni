from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Bade", None)
        self.student_2 = Student("Defne", {
            "Math": [1, 2, 3],
            "Biology": [4, 5, 6]
        })

    def test_correct_initialization(self):
        self.assertEqual("Bade", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)
        self.assertEqual("Defne", self.student_2.name)
        self.assertEqual({
            "Math": [1, 2, 3],
            "Biology": [4, 5, 6]
        }, self.student_2.courses)

    def test_enroll_adds_notes_if_course_exists(self):
        result = self.student_2.enroll("Math", [5, 6], "N")
        self.assertEqual({
            "Math": [1, 2, 3, 5, 6],
            "Biology": [4, 5, 6]
        }, self.student_2.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_adds_course_and_notes_when_add_c_notes_Y_or_empty(self):
        result_1 = self.student_1.enroll("Music", [5, 6], "Y")
        result_2 = self.student_2.enroll("Music", [9])

        self.assertEqual({"Music": [5, 6]}, self.student_1.courses)
        self.assertEqual([5, 6], self.student_1.courses["Music"])
        self.assertEqual("Course and course notes have been added.", result_1)
        self.assertEqual({
            "Math": [1, 2, 3],
            "Biology": [4, 5, 6],
            "Music": [9]},
            self.student_2.courses, self.student_2.courses)
        self.assertEqual([9], self.student_2.courses["Music"])
        self.assertEqual("Course and course notes have been added.", result_2)

    def test_enroll_adds_course_when_add_course_notes_not_Y_or_empty(self):
        result = self.student_1.enroll("Math", [0], "N")
        self.assertEqual({"Math": []}, self.student_1.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_raises_exception_if_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("Math", [4, 7])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_adds_notes_to_course(self):
        result = self.student_2.add_notes("Math", [4, 7])
        self.assertEqual({
            "Math": [1, 2, 3, [4, 7]],
            "Biology": [4, 5, 6]},
            self.student_2.courses)
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_raises_error_if_not_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_removes_course_from_courses(self):
        result = self.student_2.leave_course("Biology")
        self.assertEqual({"Math": [1, 2, 3]}, self.student_2.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == "__main__":
    main()