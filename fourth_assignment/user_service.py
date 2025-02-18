import user_utils

class UserService:
    users = {}

    def add_user(cls, user):
        if user.user_id in cls.users:
            new_id = user_utils.UserUtils.generate_user_id()
            user.set_user_id(new_id)
            cls.add_user(user)
        else:
            cls.users[user.user_id] = user

    def find_user(cls, user_id):
        return cls.users[user_id]
    
    def delete_user(cls, user_id):
        del cls.users[user_id]

    def update_user(cls, user_id, user):
        cls.users[user_id] = user
        
    @classmethod
    def get_number(cls):
        return len(cls.users)