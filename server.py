#!/usr/bin/env python3

import socket
import glob
import os
import json
HOST = input("Type in the IP address you will use to make the match: ")  # Standard loopback interface address (localhost)
PORT = input("Type in the port you will use to host the match")        # Port to listen on (non-privileged ports are > 1023)
# Grabs all the files that are in trainer_data that are json files
list_of_files = glob.glob('trainer_data/*.json') 
# Grabs the one with the latest updates and saves it to the server
newest = max(list_of_files, key = os.path.getctime)

with open(newest, "r") as loop:
        dataBox = json.load(loop)
# Opens up a socket stream for us to do stuff
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Binds the port and listens for requests
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Server is active', addr)
        print(dataBox["Name"] + " is hosting the server!")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)