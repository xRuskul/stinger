### IMPORTS ###
import socket
import sys
import time
###############

# MESSENGING #
s = socket.socket()
host = socket.gethostname()
print("Server Will Start On Host : ", host)
port = 8080
s.bind((host,port))
print("")
print("Server Is Done Binding To Host And Port Successfully!")
print("")
print("Server is waiting for incoming connections!")
print("")
s.listen(100)
conn, addr = s.accept()
print(addr, " Has connected to the server and is now online ...")
print("")
while 1:
            message = input(str(">>> "))
            message = message.encode()
            conn.send(message)
            print("System: Message Has Been Sent!")
            print("System: Waiting For Response..")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print(" Client: ", incoming_message)
            print("")
