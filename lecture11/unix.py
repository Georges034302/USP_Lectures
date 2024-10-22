#!/bin/env python3

# Read a directory from argument
# browse into the directory 
# search all the files for a pattern from STDIN 

import os, sys 

arg = sys.argv[1]
os.system('ls '+arg)

arg = os.getcwd()+'/'+arg

os.chdir(arg) # I changed directory 
os.system('pwd')

pattern = input('pattern: ')
os.system('grep -R '+pattern)
