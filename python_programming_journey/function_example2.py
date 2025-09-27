import os

os.system("clear")

def factorial(num):
    sum = 1
    while num >=1:
        sum = sum * num
        num = num - 1
        continue
    print("The Factorial of given number is: ", sum)
    print("\n")

    
values = int(input("Enter your number for factorial: "))
factorial(values)  