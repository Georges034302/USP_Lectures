import socket

# create socket server object
server_obj =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind the socket with host(IP) and port
host = '127.0.0.1'
port = 65432
server_obj.bind((host,port)) # makes the socket active listener at thios IP:port

# Start listening to broadcast/messages
server_obj.listen(1) # 1 indicates the number of accepted attempts before refusal
print(f'Server Listening on port: {port}')

# Accept connection from a client
conn, addr = server_obj.accept()
# conn used to retrieve data from client
# addr specifies the client making the connection
print(f'Connection made by {addr}')

# Receive the client data
data = conn.recv(1024).decode() # use key=1024 to decrypt the client msg
print(f'Client Message: {data}')

# Send response to client
response = 'Hello From Server'
conn.sendall(response.encode())

# close the connection
server_obj.close()
