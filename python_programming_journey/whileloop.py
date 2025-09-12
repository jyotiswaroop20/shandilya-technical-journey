import os

try:
    os.system("clear")
    x = 1
    n = int(input("Enter the number to print table - "))
    while x <= 10:
        print(x*n)
        x += 1
except ValueError:
    print("Invalid Value! Try again")
    os.system("sleep 3")
    os.system("clear")