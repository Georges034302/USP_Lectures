#!/bin/env python3

import csv  
import json 

def file_data(filename):
    data = []
    with open(filename,'r') as handler:
        csv_obj = csv.DictReader(handler)
        for row in csv_obj:
            data.append(row)
    return data  

print(file_data('students.csv'))

def save_to_json(filename,data):
    handler = open(filename,'w+')
    handler.write(json.dumps(data,indent=4))
    handler.close()

data = file_data('students.csv')
save_to_json('students.json',data)


