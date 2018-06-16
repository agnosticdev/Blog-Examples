import socket
from sys import platform

HOST = ''
PORT = 53091
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind to a blank host:port and listen for connections.
    s.bind((HOST, PORT))
    s.listen(1)
    print("Waiting for a connection...")
    conn, addr = s.accept()
    with conn:
        print('Connection bound with address: {0}'.format(addr[0]))

        while True:
            # Block and read up to 512 bytes from the read buffer.
            data = conn.recv(512)
            if not data:
                break
            else:
                read_data = len(str(data))
                if s.getblocking():
                    print("(Blocking socket) Reading {0} "
                          "bytes".format(read_data))
                else:
                    print("(Non-blocking socket) Reading {0} "
                          "bytes".format(read_data))
            conn.sendall(data)