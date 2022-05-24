name = "Bob"
greeting = f"Hello, {name}" #greeting get's set with

print(greeting)

name = "Rolf"

print(greeting)

print(f"Hello, {name}")

greetingTemplate = "Hello, {}"
withName = greetingTemplate.format(name)
withNameTwo = greetingTemplate.format("OtherName")

print(withName)
print(withNameTwo)

longerPhrase = "Hello, {}, Today is {}."
formatted = longerPhrase.format("Rolf", "Monday")

print(formatted)
