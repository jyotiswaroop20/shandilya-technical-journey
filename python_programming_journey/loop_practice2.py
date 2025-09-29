import os
def clear():
    os.system("clear")

clear()
i = 1
num = int(input("Enter your number to print table: "))
while(i <=10):
    print(num*i,end=" ")
    i += 1
print("loop stop")