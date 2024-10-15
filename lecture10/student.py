#!/bin/env python3

# Add students to students.csv where:
# Name from STDIN
# ID random integer size 6 digits
# Mark from STDIN
# Grade generated based on the mark
import csv
import random as ran  

def grade(mark):
    if mark >= 85:
        grade = "HD"
    elif mark >= 75:
        grade = "D"
    elif mark >= 65:
        grade = "C"
    elif mark >= 50:
        grade = "P"
    else:
        grade = "Z"
    return grade

def add_student(filename,ID,name,mark):
    with open(filename,'a',newline='') as handler:
        writer = csv.writer(handler)
        g = grade(mark)
        row = [ID,name,mark,g]
        writer.writerow(row)

def run():
    name = input('Name: ')
    mark = int(input('Mark: '))
    ID = ran.randint(100000,999999)
    add_student('students.csv',ID,name,mark)

run()



