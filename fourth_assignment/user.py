import user_utils
import user_service

class User:
    
    def __init__(self, name = " ", surname = " ", birthday = "01.01.2000"):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = user_utils.UserUtils.generate_email(name, surname)
        self.password = user_utils.UserUtils.generate_strong_password()
        self.user_id = user_utils.UserUtils.generate_user_id()

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_details(self):
        return f'Name: {self.name}, User ID: {self.user_id}, Surname: {self.surname}, Birthday: {self.birthday}, Email: {self.email}, Password: {self.password}'
    
    def get_age(self):
        print(user_utils.UserUtils.get_age(self.birthday))