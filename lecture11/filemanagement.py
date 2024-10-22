#!/bin/env python3

# Read a directory from STDIN
# show the absolute path
# show the directory content
# repeat the process until x is entered

import os 

def abs_path(arg):
    path = os.getcwd()
    return path+'/'+arg 

def show_content(arg):
    dirs = os.listdir(abs_path(arg))
    print(abs_path(arg))
    for item in dirs:
        print(item)
        
def run():
    arg = input('dir: ')
    
    while arg != 'x':
        show_content(arg)
        print()  
        arg = input('dir: ')

run()



