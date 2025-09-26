import os

dict = {
    "name" : "Aditya",
    "Grade": "A",
    "marks": [89,76,56]
}
os.system("clear")
dict["Address"] = "Gorakhpur"
print("Name - ",dict["name"])
print("Grade - ",dict["Grade"])
print("Marks - ",dict["marks"])
print("Address - ", dict["Address"])

print("\n")
#Nested Dictionaries
student = {
    "name" : "Aditya",
    "score": {
        "chem" : 76,
        "phy"  : 97,
        "math" : 95
    }
}
student.update({"address" : "Gorakhpur"})
print("Student Name : ", student["name"])
print("Address : ", student["address"])
print("Score List:---- ", "\nChemistry : ", student["score"]["chem"], "\nPhysics : ", student["score"]["phy"], "\nMath : ", student["score"]["math"])
print("\n")

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))