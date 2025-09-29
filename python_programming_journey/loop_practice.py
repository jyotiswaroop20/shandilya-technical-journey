import os
def clear():
    os.system("clear")

clear()
num = 1
values = int(input("Enter your number till to print even number: "))
while(num <=values):
    if num % 2 != 0: 
        print(num,end=" ")
    num += 1
print("loop stop")