import os

newset = set() #empty set syntax

os.system("clear")
value = input("Enter your value by spacing: ").split()

for v in value:
    newset.add(str(v)) #adds an element
print(newset)

newset.remove("amit") #removes the elem an
print(newset) 

newset.pop() #removes a random value
print(newset)

newset.clear() #empties the set
print(newset)