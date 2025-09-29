import os
os.system("clear")
found = False
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
num = 101
for el in list1:
    if(num == el):
        print("Value found at index: ",list1.index(el))
        print("Value you have given :" , el)
        found = True
if not found:
    print("This number is not available in list")
    
