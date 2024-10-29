import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define server address
host = '127.0.0.1'  # localhost
port = 65432

# Send a message to the server
message = "Hello, UDP Server!"
client_socket.sendto(message.encode(), (host, port))

# Receive a response from the server
data, server = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
print("Received from server:", data.decode())

# Close the client socket
client_socket.close()
