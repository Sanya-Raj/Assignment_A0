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

# List data type

x = [1,2,3]
print("ID before : " , id(x))
x.append(4)
print("ID after  : ",  id(x)) 
print("Memory ID of x is not changed in List ")


x = [1,2,3]
print("\nID before : ", id(x))
x[0] = 100
print("ID after  : " , id(x))
print("Memory ID of x is not changed in List ")

#List are mutable data type when we perform the operation on it.

#string

s = 'Hello'
print("\nID before : " ,id(s))
#concatenation occure 
s = s + ' World'
print("ID after  :", id(s))

s = s.upper()
print("\nID after upper : ", id(s))

s = s.lower()
print("\nID after lower : ", id(s))

s = s.replace("world", "Sanya")
print("\nID after replace : ", id(x))

s = "Hello World " 
s = s.strip()
print("\nID after strip : " ,id(s))

# String are immutable data type when we perform the operation on it.

#Dictionary data type

d = {"Name " : "Sanya", "age " : "20"}
print(d)
print("ID before : ", id(d))
old_id = id(d)
d["city"] = 'Ujjain '
print(d)
print("ID after : ", id(d))
print("The address of the dictionary not change ")

# Dictioary are muable data type when we perform the opeartion on it.


 













