import os

os.system("clear")
def print_value(list1):
    print("The Value of list is: ", list1)
    print("The length of list is: ", len(list1))
    print("The type of list is: ", type(list1))   
    print(list1[0:5])

print_value([1,2,4,5,6])
