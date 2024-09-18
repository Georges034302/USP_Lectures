#!/bin/env  python3

x = 2
y = 3

print(x > y)
print(x <= y)

print(x == y)   # == checks if x and y are the same object
print(x is y)   # is checks if x and y point to the same value

print(x is not y)
print(x != y)
print(not(x == y))

b = (not(x) and not(y)) or (x+3 > y)
print(b)

b = (x < y or x is y) and (y+1 > x)
print(b)
