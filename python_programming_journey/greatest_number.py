import os
class Greatestnumber:
            def __init__(self , number1, number2, number3):
                self.number1 = number1
                self.number2 = number2
                self.number3 = number3

            def check_greatest(self):
    
                if self.number1 > self.number2 and self.number1 > self.number3:
                    print(self.number1 , "is greater number")
                elif self.number2 > self.number3:
                    print(self.number2 , "is greater number")
                else:
                     print(self.number3 , "is greater number")

while True:
    try: 
        os.system("clear")       
        e1 = Greatestnumber(int(input(f"Enter your first number: ")), int(input(f"Enter your second number: ")), int(input(f"Enter your third number: ")))
        e1.check_greatest()
        break
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue