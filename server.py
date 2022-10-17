import socket

# Create socket with socket class.
master = socket.socket()
 
# Host is the IP address of master
# machine.
host = "0.0.0.0"
import logging

logging.basicConfig(filename='serverlogs.txt', filemode='a', \
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
 
# This will be the port that the
# socket is bind.
port = 8080
 
# binding the host and port to the
# socket we created.
master.bind((host, port))
 
# listen method listens on the socket
# to accept socket connection.
master.listen(1)
 
# This method accept socket connection
# from the slave machine
try:
    slave, address = master.accept()
    print("Connected to remote server")
    logging.info("Connected to remote server...")
except Exception as e:
    print("Unable to connect to remote machine", e)
    logging.info("Unable to connect to remote machine", e)

# When the slave is accepted, we can send
# and receive data in real time
while True:
    # input the command from the user
    print(">", end=" ")
    command = input()
 
    # encode the command and send it to the
    # slave machine then slave machine can
    # executes the command
    slave.send(command.encode())
 
    # If the command is exit, close the connection
    if command == "exit":
        break
 
    # Receive the output of command, sent by the
    # slave machine.recv method accepts integer as
    # argument and it denotes no.of bytes to be
    # received from the sender.
    output = slave.recv(5000)
    print(output.decode())
    logging.info(command)
    logging.info(output.decode())
 
# close method closes the socket connection between
# master and slave.
master.close()