#!/bin/env python3

import socket

server_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 65432

server_obj.bind((host,port)) # makes the socket active on this port

server_obj.listen(1) # listening to client 1 attempt before declining
print(f'Server is listening on port: {port}')

conn, addr = server_obj.accept()

print(f'Connection made by {addr}')

data = conn.recv(1024).decode()
print(f'Client message: {data}')

response = 'Hello from server'
conn.sendall(response.encode())

server_obj.close()


