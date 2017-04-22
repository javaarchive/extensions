import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.29.192', 8000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

   
    # Look for the response
    amount_received = 0
    amount_expected = 30

    while amount_received < amount_expected:
        data = sock.recv(16).decode("UTF-8")
        amount_received =1+amount_received
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
