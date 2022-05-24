from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: List[int] = []): # <--- This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades) #prints bob's grades which is very Bad

class StudentWithCorrectParameters:
    def __init__(self, name: str, grades: Optional[List[int]]= None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)

print()
bob2 = StudentWithCorrectParameters("Bob")
rolf2 = StudentWithCorrectParameters("Rolf")
bob2.take_exam(90)
print(bob2.grades)
print(rolf2.grades) #prints what you would expect