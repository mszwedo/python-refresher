def add(x, y):
    return x + y


result = add(5, 8)
print(result)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"              #bad practice to return two different types from a funtion but Python doesn't stop you

value = divide(15, 0)
print(value)

#Coding Exercise: Functions

def return_42():
    return 42

def my_function(x, y):
    return x * y
