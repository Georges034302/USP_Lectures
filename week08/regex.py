#!/bin/env python3

# Read a string from STDIN
# Read a pattern from STDIN (something to look for)
# Use match, search findall to look for the pattern
# Use sub to replace the pattern 

import re

s = input('string: ')

# Using match: matches a pattern only at the begining of a line
# pattern = input('pattern: ')
# obj = re.match(pattern, s)
# print(obj)

# Using search: matches the first occurence of a pattern
# pattern = input('pattern: ')
# obj = re.search(pattern, s)
# print(obj)

# Using findall: returns all macthes in a list
# pattern = input('pattern: ')
# obj = re.findall(pattern, s)
# print(obj)

# Using sub: replaces a pattern with replacement
pattern = input('pattern: ')
replace = input('replacement: ')
text = re.sub(pattern, replace, s,flags=re.IGNORECASE)
print(text)












