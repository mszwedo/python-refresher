class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 35)
print(bob)

#Coding Exercise: Classes and Objects
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        return sum(map(lambda item: item["price"], self.items))

store = Store("MyMarket")
store.add_item("apple", 1)
store.add_item("banana", 3)
print(store.stock_price())