number = 7
userInput = input("Enter 'y' if you would like to play: ")

if userInput in ("y", "Y"):                 #alternate way than using lower()
    userNumber = int(input("Guess the number: "))
    if userNumber == number:
        print("You guessed correctly!")
    elif number - userNumber in (1, -1):
        print("You were off by one.")
    elif abs(number - userNumber) == 1:     #just an alternate way of the above check
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")