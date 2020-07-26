import json
from battle_system import localhost
from battle_system import player_class
# def server_host_play(player1):
#     #print("Game is loading up")

# Loads objects that we need for the game to start
def local_host_play(player1, player2):
    # Loads for the first pokemon sprite
    with open(player1, "r") as loop:
                player1_data = json.load(loop)

    # Loads for the first pokemon sprite
    with open(player2, "r") as loop:
                player2_data = json.load(loop)
    player = player_class.make_data(player1)
    opponent = player_class.make_data(player2)
    localhost.start_game(player,opponent)
    