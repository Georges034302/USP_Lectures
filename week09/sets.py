# Set is a collection of any data
# Set is unordered
# Set is not indexed
# Set does not allow duplicates (items are unique)
# Set is mutable
# Syntax my_set = {item, item, item, ..., item}

my_set = {'Tom', 35, 'has', 33.5, True}

print(my_set)

# Adding elements
my_set.add('$')
print(my_set)

my_set.update(['bank','AU'])
print(my_set)

other = {'USP'}
total = my_set.union(other)
print(total)

# Removing elements
my_set.remove('$')
print(my_set)
my_set.discard('bank')
print(my_set)
my_set.pop() # Remove last element randomly placed at the end of the set at this time
print(my_set)

del my_set
try:
	print(my_set)
except NameError:
	print('Set is deleted')