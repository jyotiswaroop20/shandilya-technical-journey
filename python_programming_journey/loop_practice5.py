import os
def clear():
    os.system("clear")

clear()
i = 1
while i <= 5:
    if i == 3:
        i += 1      
        continue
        # break
    print(i)
    i += 1         