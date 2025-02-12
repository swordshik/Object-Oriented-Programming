class UserService:
    def __init__(cls, users = {}):
        cls.users = users

    def add_user(cls, user):
        cls.users[user.user_id] = user

    def find_user(cls, user_id):
        return cls.users[user_id]
    
    def delete_user(cls, user_id):
        del cls.users[user_id]

    def update_user(cls, user_id, user):
        cls.users[user_id] = user

    def get_number(cls):
        return len(cls.users)