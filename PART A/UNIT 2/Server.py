# 4. Write a program on datagram socket for client/server to display the messages on client side, typed at the server side.

import socket

HOST = '127.0.0.1'
PORT = 65432
BYTE_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    while True:
        message = input('Message = ')
        if not message:
            s.sendto(b'', (HOST, PORT))
            break
        message += '\n'
        s.sendto(message.encode(), (HOST, PORT))

    s.close()
