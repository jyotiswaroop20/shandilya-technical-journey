import os
def clear():
    os.system("clear")

clear()
num = 100
while(num >= 1):
    print(num,end=  " ")
    num -= 1
print("loop stop")