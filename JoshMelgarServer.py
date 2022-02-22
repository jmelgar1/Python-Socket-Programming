import socket

# Create socket
s = socket.socket()

#Create data variable
data = ""

# Reserve a port number
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

# Bind server to port
s.bind((SERVER, PORT))

# Socket into listen mode
s.listen(5)
print("Socket is listening")

# Establish connection with client.
c, addr = s.accept()
print('Got connection from ', addr)

# Infinite loop until it gets "end" or we stop it
while data != "end":

    # Get data from client
    data = c.recv(1024).decode()

    # Reverse data received from client
    reverseData = data[::-1]

    # Send back reversed data to client
    c.sendall(bytes(reverseData, 'utf-8'))