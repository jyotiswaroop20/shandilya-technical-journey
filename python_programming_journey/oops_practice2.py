import os

os.system("clear")

class Account:
    def __init__(self,balance,account_no):
        self.__balance = balance
        self.account_no = account_no
        print(f"Details for account no {account_no}....")

    def debit(self,debit_amount):
        self.__balance  = self.__balance - debit_amount
    
    def credit(self,credit_amount):
        self.__balance  = self.__balance + credit_amount
    
    def get_balance(self):
        return self.__balance

a1 = Account(1500,489400100118033)
print("Total balanace in a/c:", a1.get_balance())

val1 = int(input("Enter your amount to withdrawl: "))
a1.debit(val1)
print(f"Total balanace for a/c no after debited amount{val1} is:" , a1.get_balance(),"Rs")

val2 = int(input("Enter your amount to deposite: "))
a1.credit(val2)
print(f"Total balanace in a/c after credited amount{val2}:" , a1.get_balance(),"Rs")



