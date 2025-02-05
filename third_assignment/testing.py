
import personal_account

acc1 = personal_account.PersonalAccount(123, "Sultan", [], 10000)


acc1.deposit(26)
print("after adding 26 to the deposit balance is", acc1.get_balance())

acc1.withdraw(100)
print("after withdrawing 100 from the account blance is:", acc1.get_balance())

print("Current transaction history: ")
acc1.print_transaction_history()

acc1.set_account_holder("Sultanbek Mratbekov")
acc1.set_account_number(230102015)

print('\n', acc1, sep='')