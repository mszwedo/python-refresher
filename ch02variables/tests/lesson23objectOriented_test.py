import pytest
from ch02variables.lesson23objectOriented import Student


def test_initiatesStudentCorrectly():
    student = Student("Bob", (100, 90, 93, 78, 90))

    assert student.name == "Bob",                   "name is set correctly"
    assert student.grades == (100, 90, 93, 78, 90), "grades are set correctly"


def test_averageGrade():
    student = Student("Bob", (100, 90, 93, 78, 90))

    assert student.average_grades() == 90.2, "averages grades correctly"