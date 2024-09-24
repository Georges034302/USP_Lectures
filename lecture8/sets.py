#!/bin/env python3

# Set is a collection of data of any type
# Set is unordered
# Set is not indexed 
# Set does not allow duplicates (only unique elements)
# Set is mutable (changeable)
# Syntax: my_set = {item, item, ..., item}

my_set = {'AWS', 2024, True, 12.55}

print(my_set)

# Adding 
my_set.add('AU')
print(my_set)

my_set.update(['Sept', 25])
print(my_set)

# Deleting 
my_set.pop() # Radomly remove an element 
print(my_set)

my_set.remove(12.55)
print(my_set)

my_set.discard('Sept')
print(my_set)

# Joining
other_set = {'Spring', 'AU'}
total_set = my_set.union(other_set)
print(total_set)

del my_set
try:
    print(my_set)
except NameError:
    print('Set is deleted')



