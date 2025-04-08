# Read a string from STDIN
# Read a pattern to match in the string
# Show the found matches using: match, search, findall
# Replace the found matches with a replacement from STDIN using: sub

import re 

s = input("String: ")

# Find a match using: search (match first occurence of the pattern)
pattern = input('search: ')
obj = re.search(pattern,s)
print(obj)

# Find a match using: match (match first occurence of the pattern at the begining of the string only)
pattern = input('match: ')
obj = re.match(pattern,s)
print(obj)

# Find all matches using the findall function
pattern = input('find all: ')
obj = re.findall(pattern,s)
print(obj)

# Replace a match using: sub
pattern = input('pattern: ')
repl = input('replacement: ')
txt = re.sub(pattern,repl,s,flags=re.IGNORECASE)
print(txt)