import user_utils, user_service, user

def main():
    inp = int(input(print("Welcome to the User Service!\nHow can I help you?\n1. Add User\n2. Find User\n3. Delete User\n4. Update User\n5. Get Number of Users\n6. Exit")))

    if inp == 1:
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        birthday = input("Enter birthday: ")
        user_service.UserService.add_user(user.User(name, surname, birthday))
        print("User added successfully!")
        main()

    elif inp == 2:
        user_id = input("Enter user ID: ")
        passw = input("Enter password: ")
        if passw == user_service.UserService.find_user(user_id).password:
            print(user_service.UserService.find_user(user_id).get_details())
        else:
            print("Incorrect password!")
        main()
    
    elif inp == 3:
        user_id = input("Enter user ID: ")
        passw = input("Enter password: ")
        if  passw == user_service.UserService.find_user(user_id).password:
            user_service.UserService.delete_user(user_id)
            print("User deleted successfully!")
        else:
            print("Incorrect password!")
        main()

    elif inp == 4:
        user_id = input("Enter user ID: ")
        passw = input("Enter password: ")
        if passw == user_service.UserService.find_user(user_id).password:
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            birthday = input("Enter birthday: ")
            user_service.UserService.update_user(user_id, user.User(name, surname, birthday))
            print("User updated successfully!")
        else:
            print("Incorrect password!")
        main()

    elif inp == 5:
        print(user_service.UserService.get_number())
        main()

    elif inp == 6:
        print("Goodbye! Thank you for using our service!")

main()
