# Step 1: define a function to read a directory from argument
## Then list the content of that directory
# Step 2: define a function to return the word count in a file
# Step 3: define a function to handle user options:
# option -l directory (list the directory)
# option -r filename (return the file word count)

import os
import sys

#Similar to ls -l in Unix
def list_directory(directory):
	abs_path = os.path.abspath(directory)
	dir_name = os.path.basename(abs_path)
	output = [f"Directory: {dir_name} (Path: {abs_path})"]
	for item in os.listdir(directory):
		item_path = os.path.join(directory,item)
		if os.path.isdir(item_path):
			output.append(f'Directory: {item}')
		elif os.path.isfile(item_path):
			output.append(f'File: {item}')
	return '\n'.join(output)
	
def word_count(filename):
	filename = os.path.abspath(filename)
	with open(filename,'r') as fin:
		content = fin.read()
	return(len(content))

def handle_option(op, arg):
	match op:
		case '-l':
			print(list_directory(arg))
		case '-r':
			print(f'File: {arg} has {word_count(arg)} words')
		case _:
			print('Unknown option')
			
handle_option(sys.argv[1],sys.argv[2])

