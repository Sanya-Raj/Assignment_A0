# Trace the memory id using different variables and see the location is changed or not 

#integer data type 

x = 100
print("int before : " + str(id(x)))
x = 50
print("int after : " + str(id(x)))
print("Memory ID of x is change in Integer\n")

x = 60
print("int before : " + str(id(x)))
x = x + 1
print("int after : " + str(id(x)))
print("Memory ID of x is changed in Addition\n")

x = 35
print("int before : " + str(id(x)))
x = x-20
print("int after  : " + str(id(x)))
print("Memory ID of x is changed in Subtraction\n")

x = 29
print("int before : " + str(id(x)))
x = x*1
print("int after  : " + str(id(x)))
print("Memory ID of x is not changed in multiplication because value of x didn't change\n")

x = 15
print("int before : " + str(id(x)))
x = x%2
print("int after : " , str(id(x)))
print("Memory ID of x is changed in Modulus")

# Integer are immutable data types when we perform operation on it.

#Float data type 

y = 4.5
print("float before : " , str(id(y)))

y = 5.67
print("float after : " , str(id(y)))
print("ID of y is changed in Float \n ")

y = y + 2 
print("float after add operation : " , str(id(y)))
print("ID of y in add opeation is changed \n")

y = y - 4
print("float after subtr operation : " , str(id(y)))
print("ID of y in subtar oper in float is changed \n")

y = y * 10
print("float after multi operation : " , str(id(y)))
print("ID of y in multi operation in float is changed \n")

y = y / 10
print("float after div operation : " , str(id(y)))
print("ID of y in div operation in float is changed \n")

# Float are immutable data type when we perfoem the operation on it.







