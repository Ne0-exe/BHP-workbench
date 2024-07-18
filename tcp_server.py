import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define IP and port number to listen on
    server.bind((bind_ip, bind_port))

    # Start listening
    # 5 - max number of connections in queue
    server.listen(5)
    print(f'[*] Listenining on {bind_ip}:{bind_port}')
    
    # Server waiting for connection main loop 
    while True:

        # Established connection
        # client - variable for client's socket
        client, address = server.accept()
        print(f'[*] Received connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))

        # Thread for managing client's connection 
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACKKK')

if __name__ == '__main__':
    main()