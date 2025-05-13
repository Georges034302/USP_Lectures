import socket

# create a socket object
client_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to a server
host = '127.0.0.1'
port = 65432
client_obj.connect((host,port)) # initiating connect with host

# send a message to server
message = 'Hello, Server' 	# Text
client_obj.sendall(message.encode()) # Encode the message

# receive the response from server
response = client_obj.recv(1024).decode() # convert the server response back to string
print(f'Server reply: {response}')

# close the connection
client_obj.close()


