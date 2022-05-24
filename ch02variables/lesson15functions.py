def hello():
    print("Hello!")

hello()


def userAgeInSeconds():
    userAge = int(input("Enter your age: "))
    ageSeconds = userAge * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {ageSeconds}.")


print("Welcome to the age in seconds program!")
userAgeInSeconds()
print("Goodbye!")


#def print():                   #don't do this. Python doesn't stop you from using keywords.
#    print("Hello, world!")     #print here is callign the method defined above. Not python's print method


#friends = ["Rolf", "Bob"]
#def add_friends():
#    friend_name = input("Enter your friend's name: ")
#    friends = friends + [friend_name]                  #this line causes an error because it's reusing the variable name outside of the function
#add_friends()


