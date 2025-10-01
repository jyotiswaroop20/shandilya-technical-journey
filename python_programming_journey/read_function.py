import os

os.system("clear")
filename = "student_details.txt"
with open(filename, "r") as f:
    data1 = f.readline()
    data2 = f.readline()
    data3 = f.readline()
    data4 = f.readline()
    data5 = f.readline()
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    print(data5)