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
    backgrounds = [d for d in os.listdir(background_dir) if 'night' in d]
    background = random.choice(backgrounds)
    return background_dir + background
def select_music(string_of_music_dir):
    music_list = []
    for path in Path(string_of_music_dir).rglob('*.ogg'):
        path = str(path).replace("\\", "/")
        music_list.append(str(path))
    music = random.choice(music_list)
    return music

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
    if int(current_time) >= 18 or int(current_time) <= 24 or int(current_time) >= 1 or int(current_time) < 7:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "night")
    if int(current_time) >= 7 or int(current_time) <= 11:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "morning")
    if int(current_time) >= 12 or int(current_time) <= 17:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "afternoon")
        
    enemy_sprite_string = pokemon_front_render(enemy_pokemon_data)
    enemy_sprite =  pygame.image.load(enemy_sprite_string).convert_alpha()
    background = pygame.image.load(background).convert_alpha()
    system_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/system_bar.png").convert_alpha()
    hp_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
    enemy_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
    arrow = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/arrow.png").convert_alpha()
    move_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/move_bar.png").convert_alpha()
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
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
 
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
                print (str(mx) + " is the current x " + str(my) + " is the current y")
                if mx in range(128, 191) and my in range(164, 175):
                    print("mouse is over 'fight option'")
                    # Need to blip away the stuff here
                    screen.blit(move_bar, (0,160))
                    Move_1 = font.render(player1_data["Pokemon1"][1],True, BLACK)
                    screen.blit(Move_1, (4,165))
                    Move_2 = font.render(player1_data["Pokemon1"][2],True, BLACK)
                    screen.blit(Move_2, (4,180))
                    Move_3 = font.render(player1_data["Pokemon1"][3],True, BLACK)
                    screen.blit(Move_3, (65,165))
                    Move_4 = font.render(player1_data["Pokemon1"][4],True, BLACK)
                    screen.blit(Move_4, (65,180))
                # This could be done better...
                if mx in range(3, 58) and my in range(164, 172):
                    print(player1_data["Pokemon1"][1] + " is being used!")
                    pokemon1_attack = True
                if mx in range(63, 122) and my in range(162, 173):
                    print(player1_data["Pokemon1"][3] + " is being used!")
                    pokemon1_attack = True
                if mx in range(2, 58) and my in range(177, 187):
                    print(player1_data["Pokemon1"][2] + " is being used!")
                    pokemon1_attack = True
                if mx in range(65, 121) and my in range(184, 191):
                    print(player1_data["Pokemon1"][4] + " is being used!")
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
    