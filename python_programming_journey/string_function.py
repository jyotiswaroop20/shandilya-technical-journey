import os

os.system("clear")

str = "i am learing linux from Nehra from Classes"
print(str.endswith("es"))
print(str.endswith("au"))
print("\n")
str = str.capitalize()
print(str)
print(str.capitalize())

print("\n")
print(str.replace("nehra", "Shradha"))

print("\n")
print(str.find("linux"))
print(str.find("f"))

print("\n")
print(str.count("a"))
print(str.count("from"))

print("\n")
name = input("Enter your name: ")
print(name)
print(len(name))