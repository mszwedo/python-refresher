print("Comparisons: ")
#True
print(5 == 5)
print(5 >= 5)
print(5 <= 5)

#False
print(5 == 6)
print(5 > 5)
print(5 < 5)
print(10 != 10)

print()
print("lists: ")
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  #True:  compares values in the list
print(friends is abroad)  #False: compares reference
