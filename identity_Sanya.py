# Trace the memory id using different variables and see the location is changed or not 

#integer
x = 100
print("int before : " + str(id(x)))
x = 50
print("int after : " + str(id(x)))
print("Memory ID of x is change in Integer")

x = 60
print("int before : " + str(id(x)))
x = x + 1
print("int after : " + str(id(x)))
print("Memory ID of x is changed in Addition")

x = 35
print("int before : " + str(id(x)))
x = x-20
print("int after  : " + str(id(x)))
print("Memory ID of x is changed in Subtraction")

x = 29
print("int before : " + str(id(x)))
x = x*1
print("int after  : " + str(id(x)))
print("Memory ID of x is not changed in multiplication because value of x didn't change")

x = 15
print("int before : " + str(id(x)))
x = x%2
print("int after : " , str(id(x)))
print("Memory ID of x is changed in Modulus")

# Integer are immutable data types when we perform operation on it.



