import os

# example of using super() methos

os.system("clear")

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Start")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Fortuner","Diesel")
print(car1.type)
