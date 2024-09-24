#!/bin/env python3

# List is a collection of data of any type
# List is ordered  
# List is indexed 
# List allows duplicates
# List is mutable (changeable)
# Syntax: list_name = [item0, item1, ..., itemn]

my_list = ['Tom', 34, 12.5, True]

print(my_list)
print(len(my_list))

# Reading 
print(my_list[0])               # first
print(my_list[len(my_list) -1]) # last
print(my_list[1:3])             # slice of the list 

# Adding
my_list.append('$')
print(my_list)

my_list.insert(2,'$')
print(my_list)

other_list = ['CBA',2200]
total_list = my_list + other_list
print(total_list)

# Deleting
total_list.pop()    # removes last elements
print(total_list)

total_list.pop(4)   # removes by index
print(total_list)

total_list.remove(12.5)
print(total_list)

total_list.clear()
print(total_list)

del total_list  # removes the object totally from RAM
try:
    print(total_list)
except NameError:
    print('List does not exist')

print(my_list.count('$')) # how many of this value



