import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a host and port
host = '127.0.0.1'  # localhost
port = 65432
server_socket.bind((host, port))
print("UDP Server listening on port", port)

# Receive data from a client
data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
print("Received from client:", data.decode())

# Send a response back to the client
response = "Hello, Client! I received your message."
server_socket.sendto(response.encode(), addr)

# Close the server (optional, as UDP is connectionless)
server_socket.close()
