import os

def clear():
    os.system("clear")

class Airthmetic_Operation:
    clear()
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("The sum of two given number is: ", self.num1 + self.num2)

    def division(self):
        print("The devision of two given number is: ", self.num1/self.num2)

a1 = Airthmetic_Operation(int(input("Enter your first number: ")), int(input("Enter your second number: ")))
a1.add()
a1.division()