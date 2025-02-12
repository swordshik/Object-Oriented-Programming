import user_utils
import user_service

class User:
    import user_utils
    
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = user_utils.UserUtils.generate_email(name, surname)
        self.password = user_utils.UserUtils.generate_strong_password()
        self.user_id = user_utils.UserUtils.generate_user_id()

    def get_details(self):
        return f'Name: {self.name}, Surname: {self.surname}, Birthday: {self.birthday}, Email: {self.email}, Password: {self.password}, User ID: {self.user_id}'
    
    def get_age(self):
        