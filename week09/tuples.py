# Tuple is a collection of data
# Tuple is ordered
# Tuple is indexed
# Tuple allows duplicates
# Tuple is immutable (cannot add new elements)
# Syntax: my_tuple = (item-0, ..., item-n)

my_tuple = ('Tom', 23, 44.5, True)

print(my_tuple[1])

other = ('$','AU')
total = my_tuple + other
print(total)

del total

try:
	print(total)
except NameError:
	print('tuple is deleted')