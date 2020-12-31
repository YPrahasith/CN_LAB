# 4. Write a program on datagram socket for client/server to display the messages on client side, typed at the server side.

import socket

HOST = '127.0.0.1'
PORT = 65432
BYTE_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))
    print('Successfully connected to server!')

    while True:
        message, _ = s.recvfrom(BYTE_SIZE)
        if not message:
            print()
            break
        print(message.decode(), end='')

    s.close()