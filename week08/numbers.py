#!/bin/env python3

# Read a value from STDIN
# Check if the values is positive, negative, zero or not a number


value = input('Value: ')

if value.isnumeric():
    value = int(value)
    if value == 0:
        print('value is zero')
    elif value > 0:
        print('value > 0')
    else:
        print('value < 0')
else:
    print('value is NAN')
