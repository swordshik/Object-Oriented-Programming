import user_service
import user_utils
import user

class TestUserService:
        
        def test_add_user(self):
            user_service.UserService.add_user(user.User('John', 'Doe', '01.01.2000'))
            assert user_service.UserService.get_number() == 1
        
        def test_find_user(self):
            user_service.UserService.add_user(user.User('John', 'Doe', '01.01.2000'))
            assert user_service.UserService.find_user('20').get_details() == 'John Doe 01.01.2000'
        
        def test_delete_user(self):
            user_service.UserService.add_user(user.User('John', 'Doe', '01.01.2000'))
            user_service.UserService.delete_user('20')
            assert user_service.UserService.get_number() == 0
        
        def test_update_user(self):
            user_service.UserService.add_user(user.User('John', 'Doe', '01.01.2000'))
            user_service.UserService.update_user('20', user.User('Jane', 'Doe', '01.01.2000'))
            assert user_service.UserService.find_user('20').get_details() == 'Jane Doe 01.01.2000'
        
        def test_get_number(self):
            user_service.UserService.add_user(user.User('John', 'Doe', '01.01.2000'))
            assert user_service.UserService.get_number() == 1
            user_service.UserService.add_user(user.User('Jane', 'Doe', '01.01.2000'))
            assert user_service.UserService.get_number() == 2
            user_service.UserService.delete_user('20')
            assert user_service.UserService.get_number() == 1
            user_service.UserService.delete_user('21')
            assert user_service.UserService.get_number() == 0