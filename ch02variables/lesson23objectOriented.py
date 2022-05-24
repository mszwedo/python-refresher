#student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

#def average(sequence):
#    return sum(sequence) / len(sequence)

#print(average(student["grades"]))

class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 90, 93, 78, 90))
student2 = Student("Rolf", (89, 90, 93, 78, 90))

print(student.name)
print(student.grades)
print(student.average_grades())
print(student2.average_grades())