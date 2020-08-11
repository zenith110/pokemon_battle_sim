import pokepy
import json
"""
Script written by @theshinymew
Github - https://github.com/theshinymew
Modified by @zenith110
Github - https://github.com/zenith110
"""
client = pokepy.V2Client(cache="in_memory")
items_dump = []
for i in range(1, 100):
    item = client.get_item(i)
    final_item = item.name[0].upper() + item.name[1:]
    items_dump.append(final_item)


for i in range(1, 286):
    pokemon = client.get_pokemon(i)
    item = client.get_item(i)
    # get the pokemon name
    pokemonName = pokemon.name.capitalize()

    # store the base stats
    Stats = {}

    Stats["HP"] = pokemon.stats[0].base_stat
    Stats["Attack"] = pokemon.stats[1].base_stat
    Stats["Defense"] = pokemon.stats[2].base_stat
    Stats["Sp. Atk"] = pokemon.stats[3].base_stat
    Stats["Sp. Def"] = pokemon.stats[4].base_stat
    Stats["Speed"] = pokemon.stats[5].base_stat
    Stats["Type1"] = pokemon.types[0].type.name[0].upper() + pokemon.types[0].type.name[1:]
    try:
        Stats["Type2"] = pokemon.types[1].type.name[0].upper() + pokemon.types[1].type.name[1:]
    except:
        Stats["Type2"] = "None"
    #for type_grouping in pokemon.types.type.name
    # store the moves it learns
    Moves = {}

    for move in pokemon.moves:
        # get the name of the move, fix formatting
        moveName = move.move.name
        cleanName = moveName.replace('-', ' ').title()
        # get the base power
        movePower = client.get_move(moveName).power
        if movePower is None:
            Moves[cleanName] = 0
        else:
            Moves[cleanName] = movePower
    Items = {}
    for item in items_dump:
        Items[item] = 0
    """
    Sets the position manually
    """
    Morning_1_X_Pos = 0
    Morning_1_Y_Pos = 0
    Morning_2_X_Pos = 0
    Morning_2_Y_Pos = 0
    Morning_3_X_Pos = 0
    Morning_3_Y_Pos = 0
    Morning_4_X_Pos = 0
    Morning_4_Y_Pos = 0
    Morning_5_X_Pos = 0
    Morning_5_Y_Pos = 0
    Morning_6_X_Pos = 0
    Morning_6_Y_Pos = 0
    Morning_7_X_Pos = 0
    Morning_7_Y_Pos = 0
    Morning_8_X_Pos = 0
    Morning_8_Y_Pos = 0
    Afternoon_1_X_Pos = 0
    Afternoon_1_Y_Pos = 0
    Afternoon_2_X_Pos = 0
    Afternoon_2_Y_Pos = 0
    Afternoon_3_X_Pos = 0
    Afternoon_3_Y_Pos = 0
    Afternoon_4_X_Pos = 0
    Afternoon_4_Y_Pos = 0
    Afternoon_5_X_Pos = 0
    Afternoon_5_Y_Pos = 0
    Afternoon_6_X_Pos = 0
    Afternoon_6_Y_Pos = 0
    Afternoon_7_X_Pos = 0
    Afternoon_7_Y_Pos = 0
    Afternoon_8_X_Pos = 0
    Afternoon_8_Y_Pos = 0
    Night_1_X_Pos = 0
    Night_1_Y_Pos = 0
    Night_2_X_Pos = 0
    Night_2_Y_Pos = 0
    Night_3_X_Pos = 0
    Night_3_Y_Pos = 0
    Night_4_X_Pos = 0
    Night_4_Y_Pos = 0
    Night_5_X_Pos = 0
    Night_5_Y_Pos = 0
    Night_6_X_Pos = 0
    Night_6_Y_Pos = 0
    Night_7_X_Pos = 0
    Night_7_Y_Pos = 0
    Night_8_X_Pos = 0
    Night_8_Y_Pos = 0

    Front_Position = {}
    Front_Position["Morning_1"] = [Morning_1_X_Pos, Morning_1_Y_Pos]
    Front_Position["Morning_2"] = [Morning_2_X_Pos, Morning_2_Y_Pos]
    Front_Position["Morning_3"] = [Morning_3_X_Pos, Morning_3_Y_Pos]
    Front_Position["Morning_4"] = [Morning_4_X_Pos, Morning_4_Y_Pos]
    Front_Position["Morning_5"] = [Morning_5_X_Pos, Morning_5_Y_Pos]
    Front_Position["Morning_6"] = [Morning_6_X_Pos, Morning_6_Y_Pos]
    Front_Position["Morning_7"] = [Morning_7_X_Pos, Morning_7_Y_Pos]
    Front_Position["Morning_8"] = [Morning_8_X_Pos, Morning_8_Y_Pos]
    Front_Position["Afternoon_1"] = [Afternoon_1_X_Pos, Afternoon_1_Y_Pos]
    Front_Position["Afternoon_2"] = [Afternoon_2_X_Pos, Afternoon_2_Y_Pos]
    Front_Position["Afternoon_3"] = [Afternoon_3_X_Pos, Afternoon_3_Y_Pos]
    Front_Position["Afternoon_4"] = [Afternoon_4_X_Pos, Afternoon_4_Y_Pos]
    Front_Position["Afternoon_5"] = [Afternoon_5_X_Pos, Afternoon_5_Y_Pos]
    Front_Position["Afternoon_6"] = [Afternoon_6_X_Pos, Afternoon_6_Y_Pos]
    Front_Position["Afternoon_7"] = [Afternoon_7_X_Pos, Afternoon_7_Y_Pos]
    Front_Position["Afternoon_8"] = [Afternoon_8_X_Pos, Afternoon_8_Y_Pos]
    Front_Position["Night_1"] = [Night_1_X_Pos, Night_1_Y_Pos]
    Front_Position["Night_2"] = [Night_2_X_Pos, Night_2_Y_Pos]
    Front_Position["Night_3"] = [Night_3_X_Pos, Night_3_Y_Pos]
    Front_Position["Night_4"] = [Night_4_X_Pos, Night_4_Y_Pos]
    Front_Position["Night_5"] = [Night_5_X_Pos, Night_5_Y_Pos]
    Front_Position["Night_6"] = [Night_6_X_Pos, Night_6_Y_Pos]
    Front_Position["Night_7"] = [Night_7_X_Pos, Night_7_Y_Pos]
    Front_Position["Night_8"] = [Night_8_X_Pos, Night_8_Y_Pos]

    Back_Position = {}
    Back_Position["Morning_1"] = [Morning_1_X_Pos, Morning_1_Y_Pos]
    Back_Position["Morning_2"] = [Morning_2_X_Pos, Morning_2_Y_Pos]
    Back_Position["Morning_3"] = [Morning_3_X_Pos, Morning_3_Y_Pos]
    Back_Position["Morning_4"] = [Morning_4_X_Pos, Morning_4_Y_Pos]
    Back_Position["Morning_5"] = [Morning_5_X_Pos, Morning_5_Y_Pos]
    Back_Position["Morning_6"] = [Morning_6_X_Pos, Morning_6_Y_Pos]
    Back_Position["Morning_7"] = [Morning_7_X_Pos, Morning_7_Y_Pos]
    Back_Position["Morning_8"] = [Morning_8_X_Pos, Morning_8_Y_Pos]
    Back_Position["Afternoon_1"] = [Afternoon_1_X_Pos, Afternoon_1_Y_Pos]
    Back_Position["Afternoon_2"] = [Afternoon_2_X_Pos, Afternoon_2_Y_Pos]
    Back_Position["Afternoon_3"] = [Afternoon_3_X_Pos, Afternoon_3_Y_Pos]
    Back_Position["Afternoon_4"] = [Afternoon_4_X_Pos, Afternoon_4_Y_Pos]
    Back_Position["Afternoon_5"] = [Afternoon_5_X_Pos, Afternoon_5_Y_Pos]
    Back_Position["Afternoon_6"] = [Afternoon_6_X_Pos, Afternoon_6_Y_Pos]
    Back_Position["Afternoon_7"] = [Afternoon_7_X_Pos, Afternoon_7_Y_Pos]
    Back_Position["Afternoon_8"] = [Afternoon_8_X_Pos, Afternoon_8_Y_Pos]
    Back_Position["Night_1"] = [Night_1_X_Pos, Night_1_Y_Pos]
    Back_Position["Night_2"] = [Night_2_X_Pos, Night_2_Y_Pos]
    Back_Position["Night_3"] = [Night_3_X_Pos, Night_3_Y_Pos]
    Back_Position["Night_4"] = [Night_4_X_Pos, Night_4_Y_Pos]
    Back_Position["Night_5"] = [Night_5_X_Pos, Night_5_Y_Pos]
    Back_Position["Night_6"] = [Night_6_X_Pos, Night_6_Y_Pos]
    Back_Position["Night_7"] = [Night_7_X_Pos, Night_7_Y_Pos]
    Back_Position["Night_8"] = [Night_8_X_Pos, Night_8_Y_Pos]
    
    Resource_data = {}
    Resource_data["Image_dir"] = "assets/resources/graphics/pokemon_sprites/" + pokemonName + "/"
    pokemonData = {}
    pokemonData["Stats"] = Stats
    pokemonData["Moves"] = Moves
    pokemonData["Items"] = Items
    pokemonData["Resource_data"] = Resource_data
    pokemonData["Front_Position"] = Front_Position
    pokemonData["Back_Position"] = Back_Position
    print("Now dumping " + pokemonName)
    
    
    with open("../../assets/pokemon_data/" + pokemonName + ".json", "w") as write_file:
        json.dump(pokemonData, write_file, indent=1)
    