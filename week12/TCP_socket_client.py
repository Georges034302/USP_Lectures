import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # localhost
port = 65432
client_socket.connect((host, port))

# Send a message to the server
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Receive response from the server
response = client_socket.recv(1024).decode()
print("Received from server:", response)

# Close the connection
client_socket.close()
