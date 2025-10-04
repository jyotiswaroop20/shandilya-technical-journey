import os

# This is an example of multiple inheritance

os.system("clear")
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"



c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)