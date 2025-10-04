import os
os.system("clear")

class Person:
    name = "anonymous"

    @classmethod
    def change_Name(cls,name):
        cls.name = name


p1 = Person()
p1.change_Name("Aditya")
print(p1.name)
print(Person.name)