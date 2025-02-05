import personal_account

listofacc = []

def main():
    print ("Welcome to the Personal Account Management System\nPLease select the following options:\n1. Create a new account\n2. Deposit money\n3. Withdraw money\n4. Print transaction history\n5. Exit")
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
        print("Thank you for using the Personal Account Management System")

main()