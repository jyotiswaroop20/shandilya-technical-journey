class Occurence:
    def __init__(self , userstring):
        self.userstring = userstring

    def count(self):
        str = self.userstring
        print(f"The Symbol dollor occur", str.count('$'),"times")

o1 = Occurence(input(f"Enter your strings: "))
o1.count()