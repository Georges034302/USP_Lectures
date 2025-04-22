# Read command from STDIN (r/w/x)
# r - reading file content
# w - writing new string from STDIN
# x - exit

op = input('Command (r/w/x): ')

while op != 'x':
	match op:
		case 'r': 
			h = open('data.txt','r')
			content = h.read()
			h.close()
			print(content)
		case 'w':
			h = open('data.txt','a')
			s = input('string: ')
			h.write(s+'\n')
			h.close()
		case _: print('Unknown command!')
	op = input('Command (r/w/x): ')