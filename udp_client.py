import socket

target_host = "127.0.0.1"
target_port = 9997


# creating socket object:
# AF_INET - using IPv4 or host
# SOCK_DGRAM - creating udp client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending data
# sendto() - forwarding details about server we want to send data
client.sendto("AAABBBCCC", (target_host, target_port))
              
# Receiving data
# recvfrom - receiving data over udp
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
