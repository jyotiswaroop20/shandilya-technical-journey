# Tuple example----------
# value = (1,5,3,4)
# print(id(value))
# print(value)
# value[1] = 200
# print(id(value))
# print(value)    (Error generate because tuple values can not be change)

# list example------------
# value = [1,2,3,4]
# print(value)
# print(id(value)) 
# value[0] = 200
# print(value)
# print(id(value)) (successfull print value because list value can be change)

# sets example-------------
# value = {1,2,3,4}
# print(value)
# print(id(value)) 
# value[0] = 200
# print(value)
# print(id(value)) #(Error generate because sets value also can not be change)

# dictionary example--------
value = {"Name" : "Santosh", "Age" : 25}
print(value)
print(id(value))

value["City"] = "Gorakhpur"
print(value)
print(id(value)) #(successfull print value because DICT value also can be change)

value.update({"Course" : "B.Sc(IT)"})
print(value)
print(id(value))

value["Age"] = 35
print(value)
print(id(value))