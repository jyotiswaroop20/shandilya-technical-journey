import os
os.system("clear")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_average(self):
        total = 0
        for value in self.marks:
            total += value
        print(f"Hello! {self.name} your avg marks is: {round(total / 3, 2)}")

    @staticmethod
    def hello():
        print("Bhai record print ho gaya") 

s1 = Student(input("Enter your name: "), [56, 76, 89])
s1.print_average()
s1.hello()