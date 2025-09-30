import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("Enter students details......")
name = input("Enter the Name: ")
age = int(input("Enter the Age: "))
father_name = input("Enter father Name: ")
mother_name = input("Enter mother name: ")
address = input("Enter the address: ")

filename = "student_details.txt"

# File create kare agar pehli baar ho
try:
    with open(filename, "x") as f:
        pass  # empty file create
except FileExistsError:
    pass  # agar file already exist kare to ignore

# Data append kare
with open(filename, "a") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Father Name: {father_name}\n")
    f.write(f"Mother Name: {mother_name}\n")
    f.write(f"Address: {address}\n")
    f.write("-" * 30 + "\n")  # separator for next student

print("Data writing finished....")
