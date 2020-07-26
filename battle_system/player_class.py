import json
class background(object):
    def __init__(self, front_x, front_y, back_x, back_y):
        self.front_x = front_x
        self.front_y = front_y
        self.back_x = back_x
        self.back_y = back_y
class pokemon(object):
    def __init__(self, pokemon_list_name, player_data_file):
        with open(player_data_file, "r") as loop:
            player_data = json.load(loop)
        self.pokemon_list_num = pokemon_list_name
        self.name = player_data[pokemon_list_name + "_Stats"][0]
        self.HP = player_data[pokemon_list_name + "_Stats"][7]
        self.move_1 = player_data[pokemon_list_name + "_Stats"][1]
        self.move_2 = player_data[pokemon_list_name + "_Stats"][2]
        self.move_3 = player_data[pokemon_list_name + "_Stats"][3]
        self.move_4 = player_data[pokemon_list_name + "_Stats"][4]
        self.level = player_data[pokemon_list_name + "_Stats"][5]
        self.Attack = player_data[pokemon_list_name + "_Stats"][8]
        self.Defense = player_data[pokemon_list_name + "_Stats"][9]
        self.Sp_Atk = player_data[pokemon_list_name + "_Stats"][10]
        self.Sp_Def = player_data[pokemon_list_name + "_Stats"][11]
        self.front = player_data[pokemon_list_name + "_Stats"][13]
        self.back = player_data[pokemon_list_name + "_Stats"][14]
        self.icon = player_data[pokemon_list_name + "_Stats"][15]
        self.is_defeated = False
        self.turn_passed = False

        self.Morning_1 = background(player_data[pokemon_list_name + "_Morning_1"][0], player_data[pokemon_list_name + "_Morning_1"][1], player_data[pokemon_list_name + "_Morning_1"][2], player_data[pokemon_list_name + "_Morning_1"][3])
        self.Morning_2 = background(player_data[pokemon_list_name + "_Morning_2"][0], player_data[pokemon_list_name + "_Morning_2"][1], player_data[pokemon_list_name + "_Morning_2"][2], player_data[pokemon_list_name + "_Morning_2"][3])
        self.Morning_3 = background(player_data[pokemon_list_name + "_Morning_3"][0], player_data[pokemon_list_name + "_Morning_3"][1], player_data[pokemon_list_name + "_Morning_3"][2], player_data[pokemon_list_name + "_Morning_3"][3])
        self.Morning_4 = background(player_data[pokemon_list_name + "_Morning_4"][0], player_data[pokemon_list_name + "_Morning_4"][1], player_data[pokemon_list_name + "_Morning_4"][2], player_data[pokemon_list_name + "_Morning_4"][3])
        self.Morning_5 = background(player_data[pokemon_list_name + "_Morning_5"][0], player_data[pokemon_list_name + "_Morning_5"][1], player_data[pokemon_list_name + "_Morning_5"][2], player_data[pokemon_list_name + "_Morning_5"][3])
        self.Morning_6 = background(player_data[pokemon_list_name + "_Morning_6"][0], player_data[pokemon_list_name + "_Morning_6"][1], player_data[pokemon_list_name + "_Morning_6"][2], player_data[pokemon_list_name + "_Morning_6"][3])
        self.Morning_7 = background(player_data[pokemon_list_name + "_Morning_7"][0], player_data[pokemon_list_name + "_Morning_7"][1], player_data[pokemon_list_name + "_Morning_7"][2], player_data[pokemon_list_name + "_Morning_7"][3])
        self.Morning_8 = background(player_data[pokemon_list_name + "_Morning_8"][0], player_data[pokemon_list_name + "_Morning_8"][1], player_data[pokemon_list_name + "_Morning_8"][2], player_data[pokemon_list_name + "_Morning_8"][3])

        self.Afternoon_1 = background(player_data[pokemon_list_name + "_Afternoon_1"][0], player_data[pokemon_list_name + "_Afternoon_1"][1], player_data[pokemon_list_name + "_Afternoon_1"][2], player_data[pokemon_list_name + "_Afternoon_1"][3])
        self.Afternoon_2 = background(player_data[pokemon_list_name + "_Afternoon_2"][0], player_data[pokemon_list_name + "_Afternoon_2"][1], player_data[pokemon_list_name + "_Afternoon_2"][2], player_data[pokemon_list_name + "_Afternoon_2"][3])
        self.Afternoon_3 = background(player_data[pokemon_list_name + "_Afternoon_3"][0], player_data[pokemon_list_name + "_Afternoon_3"][1], player_data[pokemon_list_name + "_Afternoon_3"][2], player_data[pokemon_list_name + "_Afternoon_3"][3])
        self.Afternoon_4 = background(player_data[pokemon_list_name + "_Afternoon_4"][0], player_data[pokemon_list_name + "_Afternoon_4"][1], player_data[pokemon_list_name + "_Afternoon_4"][2], player_data[pokemon_list_name + "_Afternoon_4"][3])
        self.Afternoon_5 = background(player_data[pokemon_list_name + "_Afternoon_5"][0], player_data[pokemon_list_name + "_Afternoon_5"][1], player_data[pokemon_list_name + "_Afternoon_5"][2], player_data[pokemon_list_name + "_Afternoon_5"][3])
        self.Afternoon_6 = background(player_data[pokemon_list_name + "_Afternoon_6"][0], player_data[pokemon_list_name + "_Afternoon_6"][1], player_data[pokemon_list_name + "_Afternoon_6"][2], player_data[pokemon_list_name + "_Afternoon_6"][3])
        self.Afternoon_7 = background(player_data[pokemon_list_name + "_Afternoon_7"][0], player_data[pokemon_list_name + "_Afternoon_7"][1], player_data[pokemon_list_name + "_Afternoon_7"][2], player_data[pokemon_list_name + "_Afternoon_7"][3])
        self.Afternoon_8 = background(player_data[pokemon_list_name + "_Afternoon_8"][0], player_data[pokemon_list_name + "_Afternoon_8"][1], player_data[pokemon_list_name + "_Afternoon_8"][2], player_data[pokemon_list_name + "_Afternoon_8"][3])

        self.Night_1 = background(player_data[pokemon_list_name + "_Night_1"][0], player_data[pokemon_list_name + "_Night_1"][1], player_data[pokemon_list_name + "_Night_1"][2], player_data[pokemon_list_name + "_Night_1"][3])
        self.Night_2 = background(player_data[pokemon_list_name + "_Night_2"][0], player_data[pokemon_list_name + "_Night_2"][1], player_data[pokemon_list_name + "_Night_2"][2], player_data[pokemon_list_name + "_Night_2"][3])
        self.Night_3 = background(player_data[pokemon_list_name + "_Night_3"][0], player_data[pokemon_list_name + "_Night_3"][1], player_data[pokemon_list_name + "_Night_3"][2], player_data[pokemon_list_name + "_Night_3"][3])
        self.Night_4 = background(player_data[pokemon_list_name + "_Night_4"][0], player_data[pokemon_list_name + "_Night_4"][1], player_data[pokemon_list_name + "_Night_4"][2], player_data[pokemon_list_name + "_Night_4"][3])
        self.Night_5 = background(player_data[pokemon_list_name + "_Night_5"][0], player_data[pokemon_list_name + "_Night_5"][1], player_data[pokemon_list_name + "_Night_5"][2], player_data[pokemon_list_name + "_Night_5"][3])
        self.Night_6 = background(player_data[pokemon_list_name + "_Night_6"][0], player_data[pokemon_list_name + "_Night_6"][1], player_data[pokemon_list_name + "_Night_6"][2], player_data[pokemon_list_name + "_Night_6"][3])
        self.Night_7 = background(player_data[pokemon_list_name + "_Night_7"][0], player_data[pokemon_list_name + "_Night_7"][1], player_data[pokemon_list_name + "_Night_7"][2], player_data[pokemon_list_name + "_Night_7"][3])
        self.Night_8 = background(player_data[pokemon_list_name + "_Night_8"][0], player_data[pokemon_list_name + "_Night_8"][1], player_data[pokemon_list_name + "_Night_8"][2], player_data[pokemon_list_name + "_Night_8"][3])

# Makes our basic player class
class player_data(object):
    def __init__(self, player_data_file, enemy_sprite):
        with open(player_data_file, "r") as loop:
                player_data = json.load(loop)
        self.name = player_data["Name"]
        self.trainer_image = player_data["Image_url"]
        # Declares our lists that has the pokemon data
        self.pokemon1 = pokemon("Pokemon1", player_data_file)
        self.pokemon2 = pokemon("Pokemon2", player_data_file)
        self.pokemon3 = pokemon("Pokemon3", player_data_file)
        self.pokemon4 = pokemon("Pokemon4", player_data_file)
        self.pokemon5 = pokemon("Pokemon5", player_data_file)
        self.pokemon6 = pokemon("Pokemon6", player_data_file)
        self.pokemon_fainted = []
        self.enemy_sprite = enemy_sprite
        self.has_attacked = False
        self.has_selected = False
        self.has_switched = False
        self.pokemon_in_use = []
def make_data(data):
    end_result = player_data(data, "")
    return end_result