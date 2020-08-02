import json
import threading
from pypresence import Presence
import time
from battle_system import localhost, player_class
def server_host_play(player1):
    with open(player1, "r") as loop:
        player1_data = json.load(loop)
    
    player = player_class.make_data(player1)
    with open(player2, "r") as loop:
        player2_data = json.load(loop)

    opponent = player_class.make_data(player2)

# Loads objects that we need for the game to start
def local_host_play(player1, player2):
    discord_presence_localhost(player1, player2)
    
    
def discord_presence_localhost(player1, player2):
    # Will be stored in json file
    client_id = '711747646179770390'  # Fake ID, put your real one here
    RPC = Presence(client_id)  # Initialize the client class
    RPC.connect() # Start the handshake loop
    # Loads for the first pokemon sprite
    with open(player1, "r") as loop:
                player1_data = json.load(loop)

    # Loads for the first pokemon sprite
    with open(player2, "r") as loop:
                player2_data = json.load(loop)
    player = player_class.make_data(player1)
    opponent = player_class.make_data(player2)
    RPC.update(state="In status screen", details= player.name + " playing  vs " + opponent.name) # Set the presence
    player = player_class.make_data(player1)
    opponent = player_class.make_data(player2)
    localhost.start_game(player, opponent, RPC)
    while True:  # The presence will stay on as long as the program is running
        time.sleep(15) # Can only update rich presence every 15 seconds
    