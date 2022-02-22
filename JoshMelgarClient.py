import socket

# Create socket
s = socket.socket()

#Create inputData variable
inputData = ""

# Define port number and get IPv4 address
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

# Connect to server through local computer
s.connect((SERVER, PORT))

while inputData != "end":

    # Send data to the server
    inputData = input("Enter a word: ")
    s.sendall(bytes(inputData, 'utf-8'))

    # Get data from server
    print(s.recv(1024).decode())