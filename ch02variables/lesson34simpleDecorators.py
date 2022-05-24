import functools

user = {"username": "jose", "access_level": "guest"}    #Change "guest" to "admin" to see other values printed

def getAdminPassword():
    return "1234"

print("Calling getAdminPassword:", getAdminPassword())

if user["access_level"] == "admin":
    print(getAdminPassword())

def secureGetAdminPassword():
    if user["access_level"] == "admin":
        return "1234"

print("Calling secureGetAdminPassword:", secureGetAdminPassword())

def make_secure(accessLevel):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == accessLevel:
                return func(*args, **kwargs)
            else:
                return f"No {accessLevel} permissions for {user['username']}."

        return secure_function
    return decorator

#newGetAdminPassword = make_secure(getAdminPassword)
#print("Calling newGetAdminPassword:", newGetAdminPassword())

@make_secure("guest")
def getAdminPasswordTwo():
    return "1234"

print()
print(getAdminPasswordTwo())
print(getAdminPasswordTwo.__name__)

@make_secure("admin")
def getPassword(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print()
print(getPassword("billing"))


@make_secure("user")
def getDashboardPassword():
    return "user: user_password"