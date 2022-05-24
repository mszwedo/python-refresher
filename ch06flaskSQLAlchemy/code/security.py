from werkzeug.security import hmac
from models.user import UserModel

def authenticate(username, password):
    user: UserModel = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user

def identity(payload):
    userID = payload['identity']
    return UserModel.find_by_id(userID)
