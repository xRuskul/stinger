### IMPORTS ###
import socket
import sys
import time
from tkinter import *
###############

# Tkinter Variables #
root = Tk()
root.title("Stinger - Client")
root.iconbitmap("logo1.ico")
root.geometry('350x500+0+0')
# tb = Text(root)
# tb.pack(side=TOP)
# tb.config(state=DISABLED, relief=SUNKEN)
5
# MESSENGING #
s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
print(" Connected to chat server")
while 1:
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            #tb.config(state=NORMAL)
            #tb.insert(INSERT," Server : " + incoming_message)
            #tb.insert("")
            #tb.config(state=DISABLED)
            print(" Server : " + incoming_message)
            print("")
            message = input(str(">>> "))
            message = message.encode()
            s.send(message)
            print("System: Message Has Been Sent!")
            print("System: Waiting For Response..")
