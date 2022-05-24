numbers = [1, 3, 5]
double = [num * 2 for num in numbers]
print(double)

doubleLambda = list(map(lambda num: num * 3, numbers))
print(doubleLambda)

print()
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
startsWithS = [friend for friend in friends if friend.startswith("S")]
print(startsWithS)

startsWithSLambda = list(filter(lambda friend: friend.startswith("S"), friends))
print(startsWithSLambda)


print()
print("friends with s id: ", id(startsWithS))