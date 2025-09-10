# This program is for simple calculation----
import math
try:
    while True:
        
        name = input("Enter your name: ")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("*********This is the action You can perform*********")
        print(f"Enter the Option-A for Addition")
        print(f"Enter the Option-S for Substraction")
        print(f"Enter the Option-M for Multiplication")
        print(f"Enter the Option-D for Division")
        print(f"Enter the Option-E for Exit")

        choice = input(f"Now Enter your choice: ").upper()
        if choice == 'A':
            print(f"Hello! {name} Your choose for Addition")
            print(f"The Value of Addition is: {num1 + num2}")
            input("\nPress Enter to exit...")
            break

        elif choice == 'S':
            print(f"Hello! {name} Your choose for Substraction")
            print(f"The Value of Substraction is: {num1 - num2}")
            input("\nPress Enter to exit...")
            break
    
        elif choice == 'M':
            print(f"Hello! {name} Your choose for Multiplication")
            print(f"The Value of Multiplication is: {num1 * num2}")
            input("\nPress Enter to exit...")
            break

        elif choice == 'D':
            print(f"Hello! {name} Your choose for Division")
            print(f"The Value of Division is: {num1 / num2}")
            input("\nPress Enter to exit...")
            break

        elif choice == 'E':
            print(f"Exiting program...")
            break
        else:
            print(f"Invalid choice! Try again.")
            input("\nPress Enter to continue...")
 
except ValueError:
    print(f"Invalid! Please enter an integer.")
