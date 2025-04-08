# 1- Read a string from STDIN
# 2- Extract any digits from the string and convert it to a number
# 3- Count the number of spaces in the string

# 1- Read a String
s = input('String: ')

# 2- Extract the digits
# - Read all characters in the string
# - Check if a character is a digit
# - Add it to a separate string
# - Convert the new string to a number
temp=''
for c in s:
	if c.isnumeric():
		temp += c # updating the string number with a digital string found
print(f'Extracted number is: {temp}')

# 3- Count the number of spaces
# - Read every character in the string
# - Check if the character is a space
# - Then count it
count = 0
i = 0

while i < len(s):
	if s[i] == ' ':
		count += 1 # similar to count = count + 1
	i += 1  # similar to i = i + 1
print(f'The number of spaces is: {count}')

# Easier method to count the number of spaces
print(f'Number of spaces = {s.count(" ")}')