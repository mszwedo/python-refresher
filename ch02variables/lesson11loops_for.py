friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")


for num in range(4):
    print(f"printing number: {num}")


#Calculate Average Grade
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(f"Average grade: {total / amount}")
print(f"Average grade: {sum(grades) / amount}")


#Coding Exercise: Flow Control if and loops
numbers = range(1,9)
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(f"Even numbers: {evens}")


userInput = input("Enter your choice: ")
if userInput == "a":
    print("Add")
elif userInput == "q":
    print("Quit")