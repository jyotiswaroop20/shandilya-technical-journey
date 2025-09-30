import os 

def clear():
    os.system("clear")


def recursion_finction(n):
    clear()
    if n == 1 or n == 0:
        return 1
    else:
        return recursion_finction(n-1) *n
    
fact = recursion_finction(5)
print("Return and print factorial...")
print(fact)
