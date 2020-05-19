import pygame
import os
import json
import glob
import random
from pathlib import Path
from pypresence import Presence
import time
from datetime import datetime
BLACK = (0, 0, 0)
transparent = (0, 0, 0, 0)
def pokemon_back_render(name_of_pokemon):
    with open("battle_system/pokemon_data/" + name_of_pokemon + ".json", "r") as loop:
                mon_file = json.load(loop)
    back_string = mon_file["Graphics"]["Image_dir"] + name_of_pokemon + "_back.png"
    return back_string
def pokemon_front_render(name_of_pokemon):
    with open("battle_system/pokemon_data/" + name_of_pokemon + ".json", "r") as loop:
                mon_file = json.load(loop)
    front_string = mon_file["Graphics"]["Image_dir"] + name_of_pokemon + "_front.png"
    return front_string
def select_background(background_dir, time_tag):
    backgrounds = [d for d in os.listdir(background_dir) if time_tag in d]
    background = random.choice(backgrounds)
    return background_dir + background
def select_music(string_of_music_dir):
    music_list = []
    for path in Path(string_of_music_dir).rglob('*.ogg'):
        path = str(path).replace("\\", "/")
        music_list.append(str(path))
    music = random.choice(music_list)
    return music
def render1_attack_menu_bar(screen, background, player1_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp, move_text):
    screen.blit(background, (0,0))
    screen.blit(player1_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(level_text, (235, 124))
    screen.blit(Enemy_Level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
    screen.blit(move_text,(8, 163))
def render1_after_attack_physical(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player1_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(system_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do_text, (8, 163))
    screen.blit(level_text, (235, 124))
    screen.blit(Fight_option, (130, 165))
    screen.blit(Pokemon_option, (130, 180))
    screen.blit(Bag_option, (195, 165))
    screen.blit(Quit_option, (195, 180))
    screen.blit(Enemy_Level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
def render_moves(screen, background, player1_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player1_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(level_text, (235, 124))
    screen.blit(Enemy_Level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
def render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(Enemy_Level, (478, 124))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))
def render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(Enemy_Level, (478, 124))
    screenB.blit(FightB_option, (380, 165))
    screenB.blit(PokemonB_option, (380, 180))
    screenB.blit(BagB_option, (450, 165))
    screenB.blit(QuitB_option, (450, 180))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))
def render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(Enemy_Level, (478, 124))
    screenB.blit(FightB_option, (380, 165))
    screenB.blit(PokemonB_option, (380, 180))
    screenB.blit(BagB_option, (450, 165))
    screenB.blit(QuitB_option, (450, 180))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))
def render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player1_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(system_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do_text, (8, 163))
    screen.blit(level_text, (235, 124))
    screen.blit(Fight_option, (130, 165))
    #screen.blit(arrow, (175, 160))
    screen.blit(Pokemon_option, (130, 180))
    screen.blit(Bag_option, (195, 165))
    screen.blit(Quit_option, (195, 180))
    screen.blit(Enemy_Level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
def local_host_play(player1, player2):
    # Checks to see that the pokemons have attacked yet
    pokemon1_attack = False
    pokemon2_attack = False
    pygame.init()
    print(os.getcwd())
    with open("battle_system/battle_code/config/game_config.json", "r") as loop:
                gameconfig = json.load(loop)
    
    width = gameconfig["Resolution"]["Width"]
    height = gameconfig["Resolution"]["Height"]
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pokemon Battle Sim")
    screenB = pygame.display.set_mode((500,195), 0, 32)
    with open(player1, "r") as loop:
                player1_data = json.load(loop)
    player1_name = player1_data["Name"]
    player_pokemon_data = player1_data["Pokemon1"][0]
    player_pokemon_string = pokemon_back_render(player_pokemon_data)
    player1_sprite =  pygame.image.load(player_pokemon_string).convert_alpha()

    with open(player2, "r") as loop:
                player2_data = json.load(loop)
    enemy_pokemon_data = player2_data["Pokemon1"][0]
    enemy_name = player2_data["Name"]
    now = datetime.now()
    current_time = now.strftime("%H")
    print("Current Time =", current_time)
    if int(current_time) >= 18  or int(current_time) >= 1 and int(current_time) < 7:
        print("It's night")
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "night")
    if int(current_time) >= 7 and int(current_time) <= 11:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "morning")
    if int(current_time) >= 12 and int(current_time) <= 17:
        print("It's afternoon")
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "afternoon")
    print(background)   
    enemy_sprite_string = pokemon_front_render(enemy_pokemon_data)
    enemy_sprite =  pygame.image.load(enemy_sprite_string).convert_alpha()
    background = pygame.image.load(background).convert_alpha()
    system_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/system_bar.png").convert_alpha()
    hp_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
    enemy_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
    arrow = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/arrow.png").convert_alpha()
    move_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/move_bar.png").convert_alpha()
    move_attack_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/attack_bar.png").convert_alpha()
    font = pygame.font.SysFont(None, 12)
    what_will_you_do_text = font.render("What will " + player_pokemon_data + " do?", True, BLACK)
    level_text = font.render(str(player1_data["Pokemon1"][5]), True, BLACK)
    Fight_option = font.render("FIGHT", True, BLACK)
    Fight_rec = Fight_option.get_rect()
    Pokemon_option = font.render("POKEéMON", True, BLACK)
    Bag_option = font.render("BAG", True, BLACK)
    Quit_option = font.render("QUIT", True, BLACK)
    Enemy_Level = font.render(str(player2_data["Pokemon1"][5]), True, BLACK)
    Enemy_name = font.render(str(player2_data["Pokemon1"][0]), True, BLACK)
    Player_pokemon_name = font.render(str(player1_data["Pokemon1"][0]), True, BLACK)
    pokemon1_max_hp = font.render(str(player1_data["Pokemon1"][7]), True, BLACK)
    damage = 0
    current_health = player1_data["Pokemon1"][7]
    enemy_max_health  = player2_data["Pokemon1"][7]
    enemy_current_health  = player2_data["Pokemon1"][7]
    pokemon1_current_hp = font.render(str(current_health), True, BLACK)
    render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
    
    music_string = select_music('battle_system/battle_code/resources/music/')
    pygame.mixer.music.load(music_string)
    pygame.mixer.music.play(-1)

    playerB_sprite_string = pokemon_front_render(player_pokemon_data)
    playerB_sprite =  pygame.image.load(playerB_sprite_string).convert_alpha() 

    enemyB_sprite_string = pokemon_back_render(enemy_pokemon_data)
    enemyB_sprite =  pygame.image.load(enemyB_sprite_string).convert_alpha() 
    what_will_you_do_textB = font.render("What will " + enemy_pokemon_data + " do?", True, BLACK)
    FightB_option = font.render("FIGHT", True, BLACK)
    PokemonB_option = font.render("POKEéMON", True, BLACK)
    BagB_option = font.render("BAG", True, BLACK)
    QuitB_option = font.render("QUIT", True, BLACK)
    # Begins the second window
    enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
    enemy_max_hp = font.render(str(enemy_max_health), True, BLACK)
    render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
    isPokemon1 = True
    isPokemon2 = False
    isPokemon3 = False
    isPokemon4 = False
    isPokemon5 = False
    isPokemon6 = False
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            
        # --- Game logic should go here
        # Will be rewritten
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                #print (str(mx) + " is the current x " + str(my) + " is the current y")
                if mx in range(128, 191) and my in range(164, 175):
                    print("mouse is over 'fight option'")
                    # Need to blip away the stuff here
                    if(isPokemon1 == True):
                        screen.fill(pygame.Color("black")) # erases the entire screen surface
                        render_moves(screen, background, player1_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                        Move_1 = font.render(player1_data["Pokemon1"][1],True, BLACK)
                        screen.blit(Move_1, (4,165))
                        Move_2 = font.render(player1_data["Pokemon1"][2],True, BLACK)
                        screen.blit(Move_2, (4,180))
                        Move_3 = font.render(player1_data["Pokemon1"][3],True, BLACK)
                        screen.blit(Move_3, (65,165))
                        Move_4 = font.render(player1_data["Pokemon1"][4],True, BLACK)
                        screen.blit(Move_4, (65,180))
                        render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                # Move1 rec
                if mx in range(3, 58) and my in range(164, 172):
                    # Going to make the below rendering into a method to make it a bit tidier
                    if(isPokemon1 == True):
                        Move1 = player1_data["Pokemon1"][1]
                        with open("battle_system/move_data/" + Move1 + ".json", "r") as loop:
                            move1 = json.load(loop)
                        
                        damage = move1["Data"]["Base_Damage"]
                        status = move1["Data"]["Status"]
                        # Checks if we have a damage hitting move
                        if(status == "Damage"):
                        # Checks if have any health
                            if(enemy_current_health > 0):
                                # Take away the enemy's health
                                enemy_current_health -= damage
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                pokemon1_current_hp = font.render(str(current_health), True, BLACK)
                                move_text = font.render(player_pokemon_data + " attacks "+ enemy_pokemon_data + " with " + Move1 + " dealing " +str(damage) + " damage", True, BLACK)
                                render1_attack_menu_bar(screen, background, player1_sprite, enemy_sprite, move_attack_bar, hp_bar, enemy_bar,  level_text, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp, move_text)
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                what_will_you_do_textB = font.render(enemy_pokemon_data + " was dealt " + str(damage) + " damage from " + player_pokemon_data + "'s " + Move1, True, BLACK)
                                render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, move_attack_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                time.sleep(5)
                                screenB.fill(pygame.Color("black"))
                                what_will_you_do_textB = font.render("What will " + enemy_pokemon_data + " do?", True, BLACK)
                                render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print("Total hp is: " + str(enemy_current_health))
                                print("There's still health to go after!")
                            if(enemy_current_health <= 0):
                                screenB.fill(pygame.Color("black")) # erases the entire screen surface
                                enemy_current_health = 0
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print(enemy_pokemon_data + " has fainted!")
                        if(status == "Status-effect"):
                            print(Move1 + " causes a status, no damage taken!")
                            pokemon1_attack = True
                if mx in range(63, 122) and my in range(162, 173):
                    if(isPokemon1 == True):
                        Move2 = player1_data["Pokemon1"][2]
                        with open("battle_system/move_data/" + Move2 + ".json", "r") as loop:
                            move2 = json.load(loop)
                        
                        damage = move2["Data"]["Base_Damage"]
                        status = move2["Data"]["Status"]
                        # Checks if we have a damage hitting move
                        if(status == "Damage"):
                        # Checks if have any health
                            if(enemy_current_health > 0):
                                # Take away the enemy's health
                                enemy_current_health -= damage
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                pokemon1_current_hp = font.render(str(current_health), True, BLACK)
                                render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text,  Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                                print("Total hp is: " + str(enemy_current_health))
                                print("There's still health to go after!")
                            if(enemy_current_health <= 0):
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                enemy_current_health = 0
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print(enemy_pokemon_data + " has fainted!")
                        if(status == "Status-effect"):
                            print(Move1 + " causes a status, no damage taken!")
                            pokemon1_attack = True
                if mx in range(2, 58) and my in range(177, 187):
                    if(isPokemon1 == True):
                        Move3 = player1_data["Pokemon1"][3]
                        with open("battle_system/move_data/" + Move3 + ".json", "r") as loop:
                            move3 = json.load(loop)
                        
                        damage = move3["Data"]["Base_Damage"]
                        status = move3["Data"]["Status"]
                        # Checks if we have a damage hitting move
                        if(status == "Damage"):
                        # Checks if have any health
                            if(enemy_current_health > 0):
                                # Take away the enemy's health
                                enemy_current_health -= damage
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                pokemon1_current_hp = font.render(str(current_health), True, BLACK)
                                render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print("Total hp is: " + str(enemy_current_health))
                                print("There's still health to go after!")
                            if(enemy_current_health <= 0):
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                enemy_current_health = 0
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print(enemy_pokemon_data + " has fainted!")
                        if(status == "Status-effect"):
                            print(Move1 + " causes a status, no damage taken!")
                            pokemon1_attack = True
                if mx in range(65, 121) and my in range(184, 191):
                    if(isPokemon1 == True):
                        Move4 = player1_data["Pokemon1"][4]
                        with open("battle_system/move_data/" + Move4 + ".json", "r") as loop:
                            move4 = json.load(loop)
                        
                        damage = move4["Data"]["Base_Damage"]
                        status = move4["Data"]["Status"]
                        # Checks if we have a damage hitting move
                        if(status == "Damage"):
                        # Checks if have any health
                            if(enemy_current_health > 0):
                                # Take away the enemy's health
                                enemy_current_health -= damage
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                pokemon1_current_hp = font.render(str(current_health), True, BLACK)
                                render1_screen(screen, background, player1_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print("Total hp is: " + str(enemy_current_health))
                                print("There's still health to go after!")
                            if(enemy_current_health <= 0):
                                screen.fill(pygame.Color("black")) # erases the entire screen surface
                                enemy_current_health = 0
                                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                                render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                print(enemy_pokemon_data + " has fainted!")
                        if(status == "Status-effect"):
                            print(Move1 + " causes a status, no damage taken!")
                            pokemon1_attack = True

                if mx in range(195, 250) and my in range(164, 175):
                    print("mouse is over 'bag option'")
                if mx in range(128, 191) and my in range(180, 187):
                    print("mouse is over 'pokemon option'")
                if mx in range(194, 250) and my in range(183, 187):
                    print("mouse is over 'quit option'")
                    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
    