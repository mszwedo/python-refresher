list = ["Bob", "Rolf", "Anne"]
print(list)

tuple = ("Bob", "Rolf", "Anne")
print(tuple)

set = {"Bob", "Rolf", "Anne"}
print(set)

print(list[0])
print(tuple[2])

list[0] = "Smith"
print(list[0])

list.append("Anderson")
print(f"Length of list after append {len(list)}")

list.remove("Smith")
print(f"Length of list after remove {len(list)}")
print(list)

set.add("Smith")
set.add("Smith")                #Smith only added once because set can NOT have duplicates
print(f"New Set: {set}")