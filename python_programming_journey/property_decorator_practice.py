import os

os.system("clear")
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        final = float((self.phy + self.chem + self.math) / 3)
        return round(final,2)
    

s1 = Student(89,78,56)
print(s1.percentage,"%")
s1.phy = 98
print(s1.percentage,"%")