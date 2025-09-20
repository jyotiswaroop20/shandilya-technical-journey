import os
    
while True:
    try:
        
        os.system("clear")
        print("This program is for Calculating area of square.....")
        num1 = float(input(f"Enter the side of square: "))
        area = num1**2
        print("The Area of Square is :",area)
        break
    
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer or float value Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue