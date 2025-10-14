# Step 1: Define a function to generate a random 3-digit ID
# Step 2: Define a function to return the grade based on the mark
# Step 3: Define a function to read CSV content
# Step 4: Define a function to add a row in CSV file
# Step 5: Define a function to take two arguments:
# first is user option (-r read csv file) (-w write new row)
# second is the filename

import sys 
import random as ran 
import csv 

# step 1
def random_id():
	return ran.sample(range(100000,1000000),1)

# step 2
def grade(mark):
	if mark >= 85:
		grade = 'HD'
	elif mark >= 75:
		grade = 'D'
	elif mark >= 65:
		grade = 'C'
	elif mark >= 50:
		grade = 'P'
	else:
		grade = 'Z'
	return grade

# step 3
def read_from_csv(filename):
	with open(filename,'r') as fin:
		csv_obj = csv.reader(fin)
		for row in csv_obj:
			print(row)

# step 4
def write_to_csv(filename):
	with open(filename,'a',newline='') as fout:
		csv_writer = csv.writer(fout)
		id = random_id()[0]
		name = input('name: ')
		mark = int(input('mark: '))
		row = [id,name,mark,grade(mark)]
		csv_writer.writerow(row)

# step 5:
def handle_option(op, filename):
	match op:
		case '-r':
			read_from_csv(filename)
		case '-w':
			write_to_csv(filename)
		case _:
			print('Unknown option')

# main operation
if __name__ == '__main__':	
	handle_option(sys.argv[1], sys.argv[2])
	
