
# Read string from STDIN
# Write the string to a text file
# Read and show the file content

s = input('string: ')

# Write operation
handler = open('data.txt', 'a') # Creates data.txt and returns handler object
handler.write(s+'\n')
handler.close()

# Read operation
handler = open('data.txt', 'r')
content = handler.read()
handler.close()

print(content)