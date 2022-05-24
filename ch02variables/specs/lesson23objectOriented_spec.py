from nimoy.specification import Specification
from ch02variables.lesson23objectOriented import Student

class Lesson23objectOrientedSpec(Specification):

    def studentIsInitializedCorrectly(self):
        with when:
            student = Student("Bob", (100, 90, 93, 78, 90))

        with then:
            student.name == "Bob",                      "name is set correctly"
            student.grades == (100, 90, 93, 78, 90),    "grades are set correctly"


    def averageGradesCalculatesCorrectly(self):
        with given:
            student = Student("Bob", grades)

        with expect:
            student.average_grades() == expectedAverage

        with where:
            grades                | expectedAverage | scenario
            (100, 90, 93, 78, 90) | 90.2            | "basic average"
            (89, 90, 93, 78, 90)  | 88.0            | ""
            (78,)                 | 78              | "test one grade"
