def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)


def namedArgs(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

namedArgs(**details)
named(**details)


print()
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

print()
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)

def myFunction(**kwargs):
    print(kwargs)

myFunction(**"Bob")     #Error, must be mapping
myFunction(**None)      #Error, these are not dictionaries


#POST Example
"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""