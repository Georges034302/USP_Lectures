

# List is a collection of data
# List is ordered
# List is indexed
# List allows duplicates
# List is mutable (changeable)
# Syntax: my_list = [item-0, item-1, ..., item-n]

my_list = ['Tom',35,12.5,True]

length = len(my_list) # returns the length of the list

# Reading elements
print(f'Length = {length}')
print(f'first = {my_list[0]}')
print(f'last = {my_list[length-1]}')
print(f'slice = {my_list[1:length-1]}')

# Adding elements
my_list.append('$') # add the $ to the end of the list
print(my_list)

my_list.insert(2,'has') # Add 'has' at position 2
print(my_list)

other = ['bank', 'AU']
total = my_list + other
print(total)

# Deleting elements
total.pop() # removes the last element
print(total)

total.pop(1) # removes element at position 1
print(total)

total.remove('$') # removes element by name
print(total)

total.clear()
print(total)

del total # deletes the variable total

try:
	print(total)
except NameError:
	print('total is deleted')
	
print('Thank you')

