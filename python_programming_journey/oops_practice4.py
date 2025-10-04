import os

os.system("clear")
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   #Example of private attribute

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("489500100118033", "Software123@")
print(acc1.acc_no)
print(acc1.reset_pass())