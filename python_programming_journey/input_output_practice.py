import os
num = []
count = 0
count1 = 0
os.system("clear")
filename = "practice.txt"
with open(filename, "r") as f:
    data = f.read()
    num = data.split(",")
    print(num)
    for val in num:
        fnum = int(val)
        if fnum % 2 == 0:
            count += 1
        else:
            count1 += 1
        
    print(f"Number of even Values in list are: " ,count)
    print(f"Number of odd Values in list are: ", count1)
    print("\n")


