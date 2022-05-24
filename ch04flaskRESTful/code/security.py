from werkzeug.security import hmac
from user import User

users = [
    User(1, 'bob', 'asdf')
]

usernameMapping = {u.username: u for u in users}
userIDmapping = {u.id: u for u in users}

def authenticate(username, password):
    user: User = usernameMapping.get(username, None)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    userID = payload['identity']
    return userIDmapping.get(userID, None)
