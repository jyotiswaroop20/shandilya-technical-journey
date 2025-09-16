import os
os.system("clear")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the fthird number: "))

if a >= b and a >=c:
    print(a, "is largest number")
if b>=c:
    print(b, "is largest number")
else:
    print(c,"is largest number")


