# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 1111)  # Server IP and port

    try:
        client_socket.connect(server_address)
        message = "Hello, server! How are you doing?"
        client_socket.sendall(message.encode('utf-8'))

        data = client_socket.recv(1024).decode('utf-8')
        print("Server response:", data)

    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#     # Create a TCP/IP socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Connect the socket to the port where the server is listening
#     server_address = ('localhost', 10000)
#     # print >>sys.stderr, 'connecting to %s port %s' % server_address
#     print('connecting to %s port %s' % server_address, file=sys.stderr)
#     sock.connect(server_address)
#
#     try:
#
#         # Send data
#         message = 'This is the message. It will be repeated.'
#         # print >> sys.stderr, 'sending "%s"' % message
#         print(f'sending "{message}"', file=sys.stderr)
#         # Convert the string to a bytes-like object using UTF-8 encoding
#         message_bytes = message.encode('utf-8')
#         sock.sendall(message_bytes)
#
#         # Look for the response
#         amount_received = 0
#         amount_expected = len(message)
#
#         while amount_received < amount_expected:
#             data = sock.recv(16)
#             amount_received += len(data)
#             # print >> sys.stderr, 'received "%s"' % data
#             print(f'received "{data}"', file=sys.stderr)
#
#     finally:
#         # print >> sys.stderr, 'closing socket'
#         print('closing socket', file=sys.stderr)
#         sock.close()
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
