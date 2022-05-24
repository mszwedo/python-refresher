def add(x, y):
    return x + y

print(add(5, 7))

adding = lambda x, y: x + y
print(adding(5, 7))




def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

doubled = [double(x) for x in sequence]
print(doubled)

doubled = list(map(double, sequence))
print(doubled)

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)