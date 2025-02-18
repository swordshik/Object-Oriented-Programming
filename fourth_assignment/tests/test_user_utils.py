import user_utils as uu
import user_service as us

class TestUserUtils:
    

    def test_generate_user_id(self):
        user_id = uu.UserUtils.generate_user_id()

        print(user_id)

    def test_generate_strong_password(self):
        password = uu.UserUtils.generate_strong_password()

        print(password)