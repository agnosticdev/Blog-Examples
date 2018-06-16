import socket


HOST = 'localhost'
PORT = 53091
write_index = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except OSError as err:
        print("Client socket failed to open with error: {0}".format(err))

    while write_index < 10:
        string = "Writing data at index: {0} ".format(write_index)
        s.sendall(str.encode(string))
        # Block and write up to 512 bytes to the write buffer.
        data = s.recv(512)
        # Using bpo-32373, check to see if this socket is blocking.
        if s.getblocking():
        	print("(Blocking socket) " + data.decode())
        else:
        	print("(Non-blocking socket) " +  data.decode())

        write_index += 1

    # Close the socket, but wait.... is it really closed???
    s.close()
    # Just to make sure (bpo-32454), send data to validate that the 
    # socket is closed.
    try:
        s.sendall(str.encode('closed'))
        print("Client socket remains open")
    except OSError as err:
        print("Client socket is closed with error: {0}".format(err))
