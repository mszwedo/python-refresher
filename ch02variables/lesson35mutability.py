a = []
b = a

print(id(a))
print(id(b))

a.append(2)

print(a)
print(b)

tuple = ()
tuple = tuple + (15,) #This creates a new object. It does NOT modify the original
print(tuple)

word: str = "hello"
print(word)