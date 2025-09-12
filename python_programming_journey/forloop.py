# for i in range(10): # print value (0 ,1,2,3,4,5,6,7,8,9)
#     print(i)

# for i in range(1, 11): #it will print 2 table (2,4,6,8,10,12,14,18,20)
#     print(i*2)

# for i in range(1, 20, 2): # loop from 1 to 19, skipping by 2 each time(like 1,3,5,7,9,11,13,15,17,19)
#     print(i)
    
# for i in range(10, 0 , -1): # print value (10 ,9 ,8 ,7 , 6. 5 ,4, 3, 2, 1)
#   print(i)

input_valid = False

while not input_valid:
    x = input("Enter a number, 5-50 inclusive: ")
    x = int(x)

    if x >= 5 and x <= 50:
        input_valid = True # We got a good number!
