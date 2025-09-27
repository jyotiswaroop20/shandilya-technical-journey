import os

os.system("clear")

def print_list(list1, index=0):
    
    if index >= len(list1):
        return
    print(list1[index])
    print_list(list1,index + 1)
    print(list1[index])
    

print_list([1,2,3,4,5])