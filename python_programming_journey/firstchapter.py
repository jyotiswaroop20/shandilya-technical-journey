import os
    
while True:
    try:
        
        os.system("clear")
        print("This program is for Calculating two numbers.....")
        num1 = int(input(f"Enter your first number: "))
        num2 = int(input(f"Enter your second number: "))
        sum = num1 + num2
        print("The sum is :",sum)
        break
    
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue