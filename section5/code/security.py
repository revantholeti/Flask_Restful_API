from user import Users

def authentication(username,password):
    print(username)
    user = Users.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return Users.find_by_id(user_id)