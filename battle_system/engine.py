from battle_system import localhost
import json
# Makes our basic player class
class player_data(object):
    def __init__(self, player_data_file, enemy_sprite):
        with open(player_data_file, "r") as loop:
                player_data = json.load(loop)
        self.name = player_data["Name"]
        self.trainer_image = player_data["Image_url"]
        self.time_spent = player_data["Time_Spent"]
        # Declares our lists that has the pokemon data
        self.pokemon1 = []
        self.pokemon2 = []
        self.pokemon3 = []
        self.pokemon4 = []
        self.pokemon5 = []
        self.pokemon6 = []
        self.pokemon_fainted = []
        self.enemy_sprite = enemy_sprite
        self.is_defeated = False
        self.has_attacked = False
        for i in range(0, 16):
            self.pokemon1.append(player_data["Pokemon1"][i])
            self.pokemon2.append(player_data["Pokemon2"][i])
            self.pokemon3.append(player_data["Pokemon3"][i])
            self.pokemon4.append(player_data["Pokemon4"][i])
            self.pokemon5.append(player_data["Pokemon5"][i])
            self.pokemon6.append(player_data["Pokemon6"][i])
        for j in range(0, 1):
            self.pokemon1.append(self.is_defeated)
            self.pokemon2.append(self.is_defeated)
            self.pokemon3.append(self.is_defeated)
            self.pokemon4.append(self.is_defeated)
            self.pokemon5.append(self.is_defeated)
            self.pokemon6.append(self.is_defeated)
            
        self.pokemon1_icon = self.pokemon1[16]
        self.pokemon2_icon = self.pokemon2[16]
        self.pokemon3_icon = self.pokemon3[16]
        self.pokemon4_icon = self.pokemon4[16]
        self.pokemon5_icon = self.pokemon5[16]
        self.pokemon6_icon = self.pokemon6[16]

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
    player = player_data(player1, "")
    opponent = player_data(player2, "")
    localhost.start_game(player,opponent)
    