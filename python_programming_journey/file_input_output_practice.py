import os

def clear():
    os.system("clear")

clear()
# f = open("student.txt", "a")
# print("Writing Data in file.....")
# data = f.write("\nI am Linux Engineer.")
# print("Wrting finished in the file and closed")
# f.close()


f1 = open("student.txt","r")
data1 = f1.read()
print(data1)
f1.close()
