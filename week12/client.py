#!/bin/env python3

import socket

client_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 65432

client_obj.connect((host,port)) # start connection with server

msg = 'Hello, Server'
client_obj.sendall(msg.encode())

response = client_obj.recv(1024).decode()
print(f'Server reply: {response}')

client_obj.close()
