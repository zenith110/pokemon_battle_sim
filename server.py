#!/usr/bin/env python3

import socket
import threading
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"
list_of_players = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg recieved".encode(FORMAT))
    conn.close()



def start():
    """
    Starts the server and wait
    """
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        """
        Stores info for the users that log on
        """
        conn, addr = server.accept()
        """
        Creates a new thread so we can let the work happen on a different thread
        """
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() -1}")

print("[STARTING] SERVER IS BOOTING UP...")
start()