import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(10 ^ 24)
        data = data.decode()
        print("receiving data...")
        receive = open("file-received.jpg", 'a+b')

        received_file = connection.recv(10 ^ 24)
        while received_file:
            receive.write(received_file)
            received_file = connection.recv(10 ^ 24)

        receive.close()
        print(f"no more data from{client_address}")
        break

    # Clean up the connection
    connection.close()
