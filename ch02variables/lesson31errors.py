def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0.")
        return

    return dividend / divisor

def divideWithErrorSupport(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

divide(15, 0)

grades = [78, 99, 85, 100]
print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))
print(f"The average grade is {average}.")


grades2 = []
print()
print("Welcome to the average grade program.")
average2 = divide(sum(grades2), len(grades2))
print(f"The average grade is {average2}.")


#print()                                                #can uncomment if I want to see what the error looks like
#print("Welcome to the average grade program.")
#average2 = divideWithErrorSupport(sum(grades2), len(grades2))
#print(f"The average grade is {average2}.")

print()
print("Welcome to the average grade program.")
try:
    average2 = divideWithErrorSupport(sum(grades2), len(grades2))
except ZeroDivisionError as e:
    #print(e)
    print("There are no grades yet in yoru list.")
except ValueError:
    print("Value Error Example")
else:
    print(f"The average grade is {average2}.")
finally:
    print("Thank you!")


print()
students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    #{"name": "Rolf", "grades": [20]},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divideWithErrorSupport(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except:
    print(f"Error: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculations --")
