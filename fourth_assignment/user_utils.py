import datetime
import re
import string
import random

class UserUtils:
    
    def generate_user_id():
        return str(datetime.datetime.now().year)[2:] + str(random.randint(0, 9999999)).zfill(7)
    
    def generate_strong_password():
        characters = string.ascii_letters + string.digits + string.punctuation

        while True:
            password = ''.join(random.choice(characters) for i in range(8))

            if (re.search(r'[A-Z]', password)) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[\W_]', password):
                return password
        
    def get_age(self, user_birthday):
        self.birthday = user_birthday.replace('.', '/')
        self.birthday_datetime = datetime.strptime(self.birthday, '%d/%m/%Y')
        self.today = datetime.today()
        self.age = self.today.year - self.birthday_datetime.year - ((self.today.month, self.today.day) < (self.birthday_datetime.month, self.birthday_datetime.day))
        return self.age
        