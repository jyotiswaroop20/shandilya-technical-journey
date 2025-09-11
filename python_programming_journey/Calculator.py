# This program is for simple calculation----
import math
import os
try:
    os.system('clear')
    name = input("Enter your name: ")
    if name.isdigit() or len(name) < 3:
        print("❌ Invalid input. Please enter your full name (not numbers, not single/double character).")
    while True:      
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            print("\n")
            print("*********This is the action You can perform*********")
            print(f"Enter the Option-A for Addition")
            print(f"Enter the Option-S for Substraction")
            print(f"Enter the Option-M for Multiplication")
            print(f"Enter the Option-D for Division")
            print(f"Enter the Option-E for Exit")
            print("\n")
            choice = input(f"Now Enter your choice: ").upper()
            if choice == 'A':
                print(f"Hello! {name} Your choice for Addition")
                print(f"The Value of Addition is: {num1 + num2}")
                input("\nPress Enter to continue...")
                os.system('clear')

            elif choice == 'S':
                print(f"Hello! {name} Your choice for Substraction")
                print(f"The Value of Substraction is: {num1 - num2}")
                input("\nPress Enter to continue...")
                os.system('clear')
        
            elif choice == 'M':
                print(f"Hello! {name} Your choice for Multiplication")
                print(f"The Value of Multiplication is: {num1 * num2}")
                input("\nPress Enter to continue...")
                os.system('clear')

            elif choice == 'D':
                print(f"Hello! {name} Your choice for Division")
                print(f"The Value of Division is: {num1 / num2}")
                input("\nPress Enter to continue...")
                os.system('clear')

            elif choice == 'E':
                print(f"Exiting program...")
                os.system("sleep 2")
                os.system('clear')
                break
            else:
                print(f"❌Invalid choice! Try again.")
                os.system("sleep 3")
                os.system('clear')
                input("\nPress Enter to continue...")
                os.system('clear')
 
except ValueError:
    print(f"❌Invalid Value! Please enter an integer Only.")
    os.system("sleep 3")
    os.system('clear')
    input("\nPress Enter to Exit and try again...")