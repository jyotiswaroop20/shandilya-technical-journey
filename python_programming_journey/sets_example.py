import os

set1 = {1,2,3,4,5}
set2 = {6,7,3,9,10}

os.system("clear")

print(list(set1)[0])
print(set1)
print(set2)

print(set1.union(set2)) #combines both set values & returns new
print(set1.intersection(set2)) #combines common values & returns new