import os
class Checkmultiply:
            def __init__(self , number):
                print(f"This program is for checking number multiply by 7 or not...")
                self.number = number

            def check_multiply(self):
    
                if self.number % 7 == 0:
                    print(self.number , f"is a multiple of 7")
                else:
                    print(self.number , f"is NOT a multiple of 7")

while True:
    try: 
        os.system("clear")       
        cm1 = Checkmultiply(int(input(f"Enter your number: ")))
        cm1.check_multiply()
        break
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue