import math
import os

try:
    os.system("clear")
    # while True:
    x = math.sqrt(int(input("Enter your value for Square root: ")))
    print(x)
        # input("\nPress Enter to continue...")
        # os.system('clear')

except ValueError:
    print(f"❌Invalid! Please enter an integer.")
    os.system("sleep 3")
    os.system('clear')