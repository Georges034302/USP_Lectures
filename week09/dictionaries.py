# Dictionary is a collection of data formatted: {key : value}
# Dictionary key is unique
# Dictionary value can be duplicated
# Dictionart is indexed by keys
# Dictionary keys() function returns a list of keys
# Dictionery values() function returns a list of values()
# Syntax: data = {
# 	key-0: value-0,
# 	key-1: value-1,
# 	....
# }

import pprint as pp 


data = {
	'name': 'Tom',
	'age': 35,
	'role': 'admin'
}

print(data)
pp.pprint(data,width=40)

# Access items
print(data['age'])

# Update items
data['age'] = 55
print(data['age'])

# Add items
data['salary'] = 100000
pp.pprint(data,width=40)

# Delete items
del data['age']
pp.pprint(data,width=40)

del data 
try:
	print(data)
except NameError:
	print('data is deleted')