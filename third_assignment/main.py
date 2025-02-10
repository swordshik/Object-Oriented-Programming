import personal_account

listofacc = []

def main():

    print ("Welcome to the Personal Account Management System\nPLease select the following options:\n1. Create a new account\n2. Deposit money\n3. Withdraw money\n4. Print transaction history\n5. Change account holder name\n6. Change account number\n7. Exit")
    option = input("Enter the option: ")
    
    if option=="1":
        print("Creating a new account\nPlease enter the following details:\nAccount number:")
        account_number = int(input())
        account_holder = input("Account holder name: ")
        balance = float(input("Initial balance: "))
        listofacc.append(personal_account.PersonalAccount(account_number, account_holder, [], balance))
        print("Account has been created successfully")
        main()

    elif option=="2":
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the amount to deposit: "))
        for acc in listofacc:
            if acc.get_account_number() == account_number:
                acc.deposit(amount)
                print("Amount has been deposited successfully")
        main()
            
    elif option=="3":
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        for acc in listofacc:
            if acc.get_account_number() == account_number:
                if acc.get_balance() < amount:
                    print("Insufficient balance")
                else:
                    acc.withdraw(amount)
                    print("Amount has been withdrawn successfully")
        main()

    elif option=="4":
        account_number = int(input("Enter the account number: "))
        for acc in listofacc:
            if acc.get_account_number() == account_number:
                acc.print_transaction_history()
        main()

    elif option=="5":
        account_number = int(input("Enter the account number: "))
        account_holder = input("Enter the new account holder name: ")
        for acc in listofacc:
            if acc.get_account_number() == account_number:
                acc.set_account_holder(account_holder)
                print("Account holder name has been changed successfully")
        main()
        
    elif option=="6":
        account_number = int(input("Enter the account number: "))
        new_account_number = int(input("Enter the new account number: "))
        for acc in listofacc:
            if acc.get_account_number() == account_number:
                acc.set_account_number(new_account_number)
                print("Account number has been changed successfully")
        main()

    elif option=="7":
        print("Thank you for using the Personal Account Management System")

main()