# Read a value from STDIN
# Check if:
# - the value is a number    --> test if the number is:
#  							- positive (odd or even)
#							- negative
#							- zero
# - the value is a letter	 --> show the length of the string and first character
# - otherwise 			     --> unknown value

value = input('Value: ')

if value.isnumeric():
	if int(value) == 0:
		print('zero')
	elif int(value)%2 == 0:
		print('even')
	else:
		print('odd')
elif value.isalpha():
	print(f'First = {value[0]} - Length = {len(value)}')
else:
	print('Unknown')

	