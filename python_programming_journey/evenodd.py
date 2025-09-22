import os
class Evenodd:
            def __init__(self , number):
                self.number = number

            def check_evenodd(self):
    
                if self.number % 2 == 0:
                    print(self.number , "is even number")
                else:
                    print(self.number , "is odd number")

while True:
    try: 
        os.system("clear")       
        e1 = Evenodd(int(input(f"Enter your number: ")))
        e1.check_evenodd()
        break
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue