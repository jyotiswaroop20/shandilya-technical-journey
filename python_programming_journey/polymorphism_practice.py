import os

os.system("clear")
class Bird:
    def sound(self):
        print("Some generic bird sound")
class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")
class Crow(Bird):
    def sound(self):
        print("Caw Caw")

birds = [Bird(), Sparrow(), Crow()]
for b in birds:
    b.sound() # Output: Chirp Chirp, Caw Caw