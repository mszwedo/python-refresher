number = 7

while True:
    userInput = input("Would you like to play? (Y/n) ")

    if userInput == "n":
        break

    userNumber = int(input("Guess the number: "))
    if userNumber == number:
        print("You guessed correctly!")
    elif abs(number - userNumber) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")