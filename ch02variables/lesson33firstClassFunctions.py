from operator import itemgetter

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def getFriendName(friend):
    return friend["name"]

print("Using function:", search(friends, "Rolf Smith", getFriendName))
print("Using lambda:", search(friends, "Rolf Smith", lambda friend: friend["name"]))
print("Using itemgetter:", search(friends, "Rolf Smith", itemgetter("name")))
print(search(friends, "Bob Smith", getFriendName))