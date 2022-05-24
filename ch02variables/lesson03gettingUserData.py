#name = input("Enter your name: ")
#print(name)

sizeInput = input("How big is your house (in square feet): ")
squareFeet = int(sizeInput)
squareMeters = squareFeet / 10.8

print(squareMeters)

print(f"{squareFeet} square feet is {squareMeters:.2f} square meters.")