#!/bin/env python3

# Read a string from STDIN 
# Write the string to a text file  
# Read from the text file 
# Show the file content   

def write_to_text(filename,s):
    handler = open(filename,'a')
    handler.write(s)
    handler.write('\n')
    handler.close()

def data_from_text(filename):
    handler = open(filename,'r')
    content = handler.read()
    return content

s = input('String: ')
write_to_text('demo.txt',s)

print(data_from_text('demo.txt'))
