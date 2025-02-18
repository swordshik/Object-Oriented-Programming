import user_utils, user_service, user
from user import User
from time import sleep

user_service_instance = user_service.UserService()

def main():
    inp = int(input("Welcome to the User Service!\nHow can I help you?\n1. Add User\n2. Find User\n3. Delete User\n4. Update User\n5. Get Number of Users\n6. Exit\n"))

    if inp == 1:
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        birthday = input("Enter birthday: ")
        user = User(name, surname, birthday)
        user_service_instance.add_user(user)
        print("User added successfully!")
        print(user.get_details())
        sleep(3)
        main()

    elif inp == 2:
        if user_service_instance.get_number() == 0:
            print("No users to find!")
            sleep(3)
            main()
        else:
            user_id = input("Enter user ID: ")
            passw = input("Enter password: ")
            if passw == user_service_instance.find_user(user_id).password:
                print(user_service_instance.find_user(user_id).get_details())
            else:
                print("Incorrect password!")
            sleep(3)
            main()
    
    elif inp == 3:
        if user_service_instance.get_number() == 0:
            print("No users to delete!")
            sleep(3)
            main()
        else:
            user_id = input("Enter user ID: ")
            passw = input("Enter password: ")
            if passw == user_service_instance.find_user(user_id).password:
                user_service_instance.delete_user(user_id)
                print("User deleted successfully!")
            else:
                print("Incorrect password!")
            sleep(3)
            main()

    elif inp == 4:
        if user_service_instance.get_number() == 0:
            print("No users to update!")
            sleep(3)
            main()
        else:
            user_id = input("Enter user ID: ")
            passw = input("Enter password: ")
            if passw == user_service_instance.find_user(user_id).password:
                name = input("Enter name: ")
                surname = input("Enter surname: ")
                birthday = input("Enter birthday: ")
                user_service_instance.update_user(user_id, User(name, surname, birthday))
                print("User updated successfully!")
            else:
                print("Incorrect password!")
            sleep(3)
            main()

    elif inp == 5:
        print(user_service_instance.get_number())
        sleep(3)
        main()

    elif inp == 6:
        print("Goodbye! Thank you for using our service!")

main()