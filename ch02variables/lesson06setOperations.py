friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

localFriends = friends.difference(abroad)
print(localFriends)

#emptySet
print(f"Empty Set printed looks like this: {abroad.difference(friends)}")

local = {"Rolf"}

totalFriends = local.union(abroad)
print(f"Total Friends: {totalFriends}")

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(f"Study both art and science: {both}")


#Coding Exercise for Lists, Tuples, and Sets #####################################

my_list = [20, 30, 50]
my_tuple = (25,)
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

set3 = set1.intersection(set2)
print(f"Set 3: {set3}")