import socket

HOST = ""  # Symbolic name meaning all available interfaces
PORT = 55007  # Arbitrary non-privileged port

if __name__ == "__main__":
    # Create socket for IPv4 address family and 'stream' socket type
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to (HOST, PORT)
        s.bind((HOST, PORT))

        # Enable server to accept connections, allowing at most one connection
        s.listen(1)

        # Accept a connection
        conn, addr = s.accept()

        with conn:
            print(f"Connected accepted from {addr}")

            # Receive data from socket
            data = conn.recv(1024)

            try:
                file = open(data.decode("UTF-8"), "r")
                contents = file.read()
                file.close()

            except FileNotFoundError as error:
                contents = f"ERROR: {error}"

            conn.sendall(bytes(contents, "UTF-8"))
