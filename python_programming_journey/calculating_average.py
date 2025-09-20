import os
    
while True:
    try:
        
        os.system("clear")
        print("This program is for Calculating average of two numbers.....")
        num1 = float(input(f"Enter your first number: "))
        num2 = float(input(f"Enter your second number: "))
        average = (num1 + num2) / 2
        print("The average is :",average)
        break

    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 4")
        os.system("clear")
        input("Press enter to continue.....")
        os.system("clear")
        continue