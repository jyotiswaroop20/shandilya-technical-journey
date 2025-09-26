import os

user = {}
os.system("clear")
user["name"] = input("Enter Name : ")
user["age"] = int(input("Enter age : "))
user["mark"] = int(input("Enter your physics marks: "))
user["percentage"] = float(input("Enter your percentage: "))
print("\n")
print("User Name : ", user["name"])
print("Age : ", user["age"])
print("Physics Mark : ", user["mark"])
print("Percentage : ", user["percentage"],"%")
print("\n")