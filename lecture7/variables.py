#!/bin/env python3

# Python types are inferred --> value decides the type
a = 3           # int
print(a)
print(type(a))
a = 2.5         # float
print(a)
print(type(a))
a = "Hello"     # string
print(a)
print(type(a))
a = True        # boolean
print(a)
print(type(a))

#====================
a = '4'         
print(type(a))
print(type(int(a)))
b = 2.8
# Add a and be as integers only
print(int(a) + int(b)) # integers result, the int(b) removes the decimal points from b

# Convert a + b to float
print(float(int(a) + b))
print(int(a) + b) # a int and b float (2.8) --> this will lead to auto-promotion to the bigger type (float)

#==================== Error handling
a = '23'
b = 4
try:
    print(a+b)      # Cannot join string with int--> error
except TypeError:
    print('Cannot join str with int!!!')
print(a+str(b)) # converting b to string then joining

#=================== operators
a = 5
b = 2

x = a + 2 # ---> x = 7
x = x + a # ---> x = 12
x += a    # equivalent to the above

x -= 3    # x = x - 3
x *= 4    # x = x * 4
x /= 2    # x = x / 2

# ================== order of precedence
x = a * 3 + b   # x = ?
print(x)
x = a * (3 + b) # x = ?
print(x)







