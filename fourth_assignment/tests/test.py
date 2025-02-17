import datetime, random, string

today = str(datetime.datetime.now())[8:10] + '.' + str(datetime.datetime.now())[5:7] + '.' + str(datetime.datetime.now())[:4]

dateofbirth = '19.02.2006'

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def get_details():
    return f'Name: {self.name}\nSurname: {self.surname}\nBirthday: {self.birthday}\nPassword: {self.password}'