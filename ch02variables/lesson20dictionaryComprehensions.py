users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Bob"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your credentials are correct!")
else:
    print("Your credentials are inccorect.")

#Coding Exercise: Dictionaries and Students ######################################

student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}

def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])

    return total / count

