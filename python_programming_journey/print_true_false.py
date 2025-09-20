import os
    
while True:
    try:
        
        os.system("clear")
        print("This program is for printing boolean values.....")
        a = int(input(f"Enter your first number: "))
        b = int(input(f"Enter your second number: "))
        if a >= b:
            print("True")
        else:
            print("False")
        break
    
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue