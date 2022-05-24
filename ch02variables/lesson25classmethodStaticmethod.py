class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

test = ClassTest()
test.instance_method()

ClassTest.class_method()

ClassTest.static_method()

#Factory Example
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, cls.TYPES[1], page_weight)

book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)

hardcover = Book.hardcover("Harry Potter", 1500)
print(hardcover)

paperback = Book.paperback("Python 101", 600)
print(paperback)

print(Book.TYPES)

#Coding Exercise: @classmethod and @staticmethod
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        return sum(map(lambda item: item.get("price", 0), self.items))
        #total = 0
        #for item in self.items:
        #    total += item["price"]
        #return total

    @classmethod
    def franchise(cls, store):
        return Store(f"{store.name} - franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"

store = Store("Test")
store2 = Store("Amazon")
store2.add_items("Keyboard", 160)

new_store = Store.franchise(store)
new_store2 = Store.franchise(store2)

print(Store.store_details(store))
print(Store.store_details(store2))
