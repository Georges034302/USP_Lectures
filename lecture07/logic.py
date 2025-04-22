#!/bin/env python3

x = 2
y = 3

# Logical Operators: >, >=, <, <=, ==, !=, !, is, is not, not, and, or 

print(x > y)
print(x <= y)
print(x >= y)

print(x == y) # == checks if x and y point to same object
print(x is y) # is checks if x and y have the same value

print(x is not y)
print(x != y)
print(not(x == y))
print(not(x is y))

b = (not(x) and not(y)) or (x+2 > y)
print(b)

b = (x < y or x is y) and (y+1 > x)
print(b)




