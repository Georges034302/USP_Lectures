import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
host = '127.0.0.1'  # localhost
port = 65432
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port", port)

# Accept a connection from a client
conn, addr = server_socket.accept()
print("Connected by", addr)

# Receive data from the client
data = conn.recv(1024).decode()
print("Received from client:", data)

# Send a response back to the client
response = "Hello, Client! I received your message."
conn.sendall(response.encode())

# Close the connection
conn.close()
server_socket.close()
