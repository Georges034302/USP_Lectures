#!/bin/env python3

# Python types are inferred --> value decides the type 
a = 2
print(a)
print(type(a))

a = 2.5
print(a)
print(type(a))

a = True
print(a)
print(type(a))

a = '2'
print(a)
print(type(a))
print(type(int(a)))

a = 2
print(a)
print(type(a))
print(type(float(a)))
print('a = '+str(float(a)))

a = 2
x = 2
x += a # x = x + a
print(x)

x *= a # x = x * a
print(x)

x /= a # x = x / a  (float)
print(x)

x -= a # x = x - a 
print(x)

x = x**a 
print(x)
print(pow(x,a))



