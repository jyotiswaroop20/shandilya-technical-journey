# Today i will make some interesting-----
# a = "9"
# y = float(a)
# print(type(a))
# print(type(y))
# print(y)


try:
    x = input("Enter the first number: ")
    x = int(x)
    y = input("Enter your second number: ")
    y = int(y)
    print ("The some of two number is : ", x + y)
except ValueError:
    print("Invalid! Please enter an integer.")