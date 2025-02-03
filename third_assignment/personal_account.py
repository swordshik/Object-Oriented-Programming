import datetime
from amount import Amount

class PersonalAccount:
    
    def __init__(self, account_number, account_holder, transactions, balance = 0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__transactions = transactions

    def deposit(self, amount):
        moneys = Amount(amount, datetime.datetime.now(), "Deposit")
        self.__transactions.append(moneys)
        self.__balance += moneys.amount

    def withdraw(self, amount):
        moneys = Amount(amount, datetime.datetime.now(), "Withdraw")
        self.__transactions.append(moneys)
        self.__balance -= moneys.amount

    def print_transaction_history(self):
        for transaction in self.__transactions:
            print(transaction)
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self, account_number):
        self.__account_number = account_number
    
    def get_account_holder(self):
        return self.__account_holder
    
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def __str__(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: {self.__balance}"
    
    def __add__(self, amount):
        self.deposit(amount)
        return self
    
    def __sub__(self, amount):
        self.withdraw(amount)