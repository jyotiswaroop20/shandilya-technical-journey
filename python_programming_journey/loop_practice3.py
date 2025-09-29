import os
def clear():
    os.system("clear")

clear()
i = 0
j = 0
list1 = []
# number_of_values = int(input("How many values to be store in list: "))
while True:
    try:
        values = input("enter your value by spacing: ").split()
        list1 = [int(x) for x in values]

# while(j<number_of_values):
#     values = input("enter your value: ")
#     list1.insert(j,values)
#     j+=1
        print(list1)
        while (i < len(list1)): #9
            print(f"index number {i} values", list1[i])
            i += 1
        break
    except ValueError:
        print("Invalid values! , Values should be in integer")
        continue
    