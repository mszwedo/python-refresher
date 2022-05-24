from werkzeug.security import hmac
from user import User

def authenticate(username, password):
    user: User = User.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user

def identity(payload):
    userID = payload['identity']
    return User.find_by_id(userID)
