import socket

HOST = "127.0.0.1"  # The remote host
PORT = 55007  # The same port as used by the server


if __name__ == "__main__":
    filename = input("Enter filename: ")

    # Create socket for IPv4 address family and 'stream' socket type
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the remote socket (in this case, server)
        s.connect((HOST, PORT))

        # Send the file name to the server
        s.sendall(bytes(filename, "UTF-8"))

        contents = ""

        while True:
            # Receive data from the socket, 1024 bytes at a time
            data = s.recv(1024)

            if not data:
                break

            contents += data.decode("UTF-8")

    print(f"Contents of file '{filename}'':\n\n{contents}")
