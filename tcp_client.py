# Assumptions:
# 1. Establishing the connection is always successful
# 2. Server will wait for receiving data
# 3. Server will always respond quickly

import socket

target_host = "www.google.com"
target_port = 80


# creating socket object:
# AF_INET - using IPv4 or host
# SOCK_STREAM - creating tcp client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting with server
client.connect((target_host, target_port))

#sending data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode(encoding='utf-8'))

# receiving data
# recv - receiving data over tcp
response = client.recv(4096)

print(response.decode())
client.close()