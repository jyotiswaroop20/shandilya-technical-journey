import os
def clear():
    os.system("clear")

clear()
i = 0
tuple1 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100,16,16)
print("This is list of values, tell me which number u want to search: ", tuple1)

num = int(input("Enter your number: "))
found = False
while(i<len(tuple1)):
    if(tuple1[i] == num):
        print(f"Value found at index number {i}", f"and value is: {tuple1[i]}")
        found = True
    i += 1
if not found:
    print("❌ Value not found in the tuple.")
            
    
   
        

