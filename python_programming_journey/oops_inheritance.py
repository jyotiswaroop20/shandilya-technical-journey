import os
# Example of Inheritance and multilevel inheritance
os.system("clear")

class Car:
    color = "Red"
    @staticmethod
    def start():
        print("Car Start")

    @staticmethod
    def stop():
        print("Car stopped")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type =type
        


f1 = Fortuner("Diesel")
print(f1.type)

print(f1.start())
