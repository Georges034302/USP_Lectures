#!/bin/env python3

import csv 
import pandas as pd 

def read_from_csv(filename):
    with open(filename,'r') as handler:
        csv_object = csv.reader(handler)
        for row in csv_object:
            print(row)

read_from_csv('students.csv')

def write_to_csv(filename,ID,name,mark,grade):
    with open(filename,'a') as handler:
        csv_writer = csv.writer(handler)
        row = [ID,name,mark,grade]
        csv_writer.writerow(row)

write_to_csv('students.csv',123456,'Thomas Muller',78,'D')   

def read_csv_pandas(filename):
    data = pd.read_csv(filename)
    print(data)

read_csv_pandas('students.csv')


