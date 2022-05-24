moviesWatched = {"The Matrix", "Green Book", "Her"}
userMovie = input("Enter something you've watched recently: ")

if userMovie in moviesWatched:
    print(f"I've watched {userMovie} too!")
else:
    print("I haven't watched that yet.")


