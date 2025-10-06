# name = input("Enter your Name: ")


# if name:
#     print("Hello!", name)
# else:
#     print("Your have not given any name")


# for i in range(11,0,-2):
#     print(i)

# 

import sys
while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
print('You typed ' + response + '.')