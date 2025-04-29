# Get the operation and filename from argument, then perform the following operations
# if operation is -s then show the file content
# if operation is -c then show the word count

import sys 

op = sys.argv[1]
file = sys.argv[2]

def word_count(file):
	count = 0
	handler = open(file,'r')
	content = handler.readlines()
	for line in content:
		count += len(line.split(' '))
	handler.close()
	return count

def show_content(file):
	handler = open(file,'r')
	content = handler.read()
	handler.close()
	print(content)

def run():
	if op == '-r':
		show_content(file)
	elif op == '-c':
		print(f'Word count = {word_count(file)}')
	else:
		print('Possible incorrent arguments!')
run()