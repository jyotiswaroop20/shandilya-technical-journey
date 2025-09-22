# print("Hello" + "World")

str = "Apple"

# print(len(str))
# print(str[0])
# print(str[1])

# # slicing
# print(str[1:4])
# print(str[:4])
# print(str[1:])

# #negative slicing
# print(str[-3:-1])
# print(str[:-2])
# print(str[-2:])

# string function
str1 = "i am a coder"
a = str1.endswith("or")
if a == True:

    print("Hello")
    b = str1.capitalize()
    d = str1.find("am")
    print(d)
    print(b)
else:
    print("No hello")
    e = str1.count("am")
    print(e)
    c = str1.replace("am", "was")
    print(c)
