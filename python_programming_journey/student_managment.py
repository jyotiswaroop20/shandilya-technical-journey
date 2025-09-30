import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

    
clear()
filename = "student_details.txt"
with open(filename, "r") as f:
    data = f.read()
    data = data.replace("Gorakhpur", "Lucknow")

with open(filename, "w") as f:
    f.write(data)

print("Replacement done!")

with open(filename, "r") as f:
    data = f.read()
    search = "Tripathi"
    if search in data: 
        print("Data mil gaya bhai")
    else:
        print("data nahi mila bhai")

    