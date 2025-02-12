import user_utils as uu

class TestUserUtils:
    
    def test_generate_user_id():
        user_id = uu.UserUtils.generate_user_id()

        print(user_id)

    def test_generate_strong_password():
        password = uu.UserUtils.generate_strong_password()

        print(password)

    def test_generate_email(self):
        email1 = uu.UserUtils.generate_email('Sultanbek', 'Muratbekov')
        email2 = uu.UserUtils.generate_email('Sultanbek', 'Muratbekov', 'gmail.com')

        print(email1, email2)


TestUserUtils.test_generate_user_id()

TestUserUtils.test_generate_strong_password()
