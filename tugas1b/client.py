import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    file = "file.jpg"
    sock.sendall(file.encode())

    # Look for the response
    receive = open("file-received.jpg", 'a+b')

    received_file = sock.recv(10 ^ 24)
    while received_file:
        receive.write(received_file)
        received_file = sock.recv(10 ^ 24)

    receive.close()
    print("File received")

finally:
    print("closing")
    sock.close()