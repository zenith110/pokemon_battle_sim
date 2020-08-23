import pygame
from pypresence import Presence
import time
from datetime import datetime
import glob
import random
from pathlib import Path
import os
import json
from pygame.locals import *
import sys
from battle_system.localhost_utils import moves_util
BLACK = (0, 0, 0)
"""
Selects the background using a util function
@background_dir - string
@time_tag - string
return - completed background dir
"""
def select_background(background_dir, time_tag):
    backgrounds = [d for d in os.listdir(background_dir) if time_tag in d]
    background = random.choice(backgrounds)
    return background_dir + background

"""
Removes everything but the name of the background
"""
def background_trimmer(background):
    trim = background.replace("assets/resources/graphics/battle_backgrounds/", "")
    trim = trim.replace(".png", "")
    trim = trim[:1].upper() + trim[1:]
    return trim
"""
Used to load the first instance of the state
"""
def pokemon_player_battle_state(player_pokemon, opponent_pokemon, screen, screenB):
    clock = pygame.time.Clock()
    now = datetime.now()
    current_time = now.strftime("%H")
    """
    Uses time and determines what background it will be based on keywords
    """
    if int(current_time) >= 18  or int(current_time) >= 1 and int(current_time) < 7:
        background = select_background("assets/resources/graphics/battle_backgrounds/", "Night")
    elif int(current_time) >= 7 and int(current_time) <= 11:
        background = select_background("assets/resources/graphics/battle_backgrounds/", "Morning")
    elif int(current_time) >= 12 and int(current_time) <= 17:
        background = select_background("assets/resources/graphics/battle_backgrounds/", "Afternoon")
    
    background_stand_alone = background_trimmer(background)
    with open("assets/pokemon_data/" + player_pokemon.name + ".json", "r") as loop:
            player_data = json.load(loop)

    with open("assets/pokemon_data/" + opponent_pokemon.name + ".json", "r") as loop:
            opponent_data = json.load(loop)

    player_background_front_x = player_data["Front_Position"][background_stand_alone][0] + 400
    player_background_front_y = player_data["Front_Position"][background_stand_alone][1] + 50
    player_background_back_x = player_data["Back_Position"][background_stand_alone][0] - player_data["Back_Position"][background_stand_alone][0]
    player_background_back_y = player_data["Back_Position"][background_stand_alone][1] - player_data["Back_Position"][background_stand_alone][1] + 100 
    

    opponent_background_front_x = opponent_data["Front_Position"][background_stand_alone][0] - opponent_data["Front_Position"][background_stand_alone][0] - 160
    opponent_background_front_y = opponent_data["Front_Position"][background_stand_alone][1] - opponent_data["Front_Position"][background_stand_alone][1] + 75
    opponent_background_back_x = opponent_data["Back_Position"][background_stand_alone][0] 
    opponent_background_back_y = opponent_data["Back_Position"][background_stand_alone][1]

    
    background = pygame.image.load(background).convert_alpha()
    system_bar = pygame.image.load("assets/resources/graphics/battle_ui/system_bar.png").convert_alpha()
    hp_bar = pygame.image.load("assets/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
    enemy_bar = pygame.image.load("assets/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
    move_bar = pygame.image.load("assets/resources/graphics/battle_ui/move_bar.png").convert_alpha()
    move_attack_bar = pygame.image.load("assets/resources/graphics/battle_ui/attack_bar.png").convert_alpha()
    font = pygame.font.SysFont('arial', 10)
    fight_option = font.render("FIGHT", True, BLACK)
    pokemon_option = font.render("POKEéMON", True, BLACK)
    bag_option = font.render("BAG", True, BLACK)
    quit_option = font.render("QUIT", True, BLACK)
    enemy_name = font.render(opponent_pokemon.name, True, BLACK)
    player_pokemon_name = font.render(player_pokemon.name, True, BLACK)

    player_pokemon_max_hp = font.render(str(player_pokemon.HP), True, BLACK)
    player_pokemon_current_hp = font.render(str(player_pokemon.HP), True, BLACK)

    what_will_you_do = font.render("What will " + player_pokemon.name + " do?", True, BLACK)
    player_pokemon_level = font.render(str(player_pokemon.level), True, BLACK)
    enemy_level = font.render(str(opponent_pokemon.level), True, BLACK)

    fight_rec = Rect(130, 165, 20, 10)
    pokemon_rect = Rect(130, 180, 20, 10)
    bag_rect = Rect(195, 165, 20, 10)
    quit_rect = Rect(195, 180, 20, 10)

    opponent_fight_rec = Rect(380, 165, 20, 10)
    opponent_pokemon_rect = Rect(380, 180, 20, 10)
    opponent_bag_rect = Rect(450, 165, 20, 10)
    opponent_quit_rect = Rect(450, 180, 20, 10)


    player_sprite_back = pygame.image.load(player_pokemon.back)
    opponent_sprite_front = pygame.image.load(opponent_pokemon.front)
    player_sprite_front = pygame.image.load(player_pokemon.front)
    opponent_sprite_back = pygame.image.load(opponent_pokemon.back)
    screen.blit(background, (0,0))
    screen.blit(background, (250, 0))
    screen.blit(player_sprite_back, (player_background_back_x ,player_background_back_y))
    screen.blit(player_sprite_front, (player_background_front_x, player_background_front_y))
    # print("player_background_front_x: " + str(player_background_front_x) + "\nplayer_background_front_y: " + str(player_background_front_y))
    # print("player_background_back_x:" + str(player_background_back_x) + "\nplayer_background_back_y: " + str(player_background_back_y))
    screen.blit(opponent_sprite_front, ((10 - opponent_background_front_x) , (opponent_background_front_y - 20)))
    # print("opponent_background_front_x: " + str(opponent_background_front_x) + "\nopponent_background_front_y: " + str(opponent_background_front_y))
    # print("opponent_background_back_x:" + str(opponent_background_back_x) + "\nopponent_background_back_y: " + str(opponent_background_back_y))
   
    what_will_you_do_textB = ("What will " + opponent_pokemon.name + " do?", True, BLACK)
    screen.blit(system_bar, (0,160))
    screen.blit(system_bar, (250, 160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do, (8, 163))
    screen.blit(player_pokemon_level, (205, 124))

    screen.blit(fight_option, (130, 165))
    screen.blit(pokemon_option, (130, 180))
    screen.blit(bag_option, (195, 165))
    screen.blit(quit_option, (195, 180))

    screen.blit(fight_option, (380, 165))
    screen.blit(pokemon_option, (380, 180))
    screen.blit(bag_option, (450, 165))
    screen.blit(quit_option, (450, 180))

    screen.blit(enemy_level, (81, 32))
    screen.blit(enemy_name, (0, 30))
    screen.blit(player_pokemon_name, (150, 125))
    screen.blit(player_pokemon_max_hp, (215, 142))
    # screen.blit(pokemon_, (195, 144))
    carryOn = True
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            if pygame.key.get_pressed()[pygame.K_q]:
                print("The quit key has been used!")
                pygame.quit()
                sys.exit() 
        # --- Game logic should go here
        # Will be rewritten
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                Fight check for both sides, due to player picking whichever after
                """
                if fight_rec.collidepoint(mouse_pos):
                    player_pokemon.has_selected = True
                    if(player_pokemon.has_selected and opponent_pokemon.has_selected):
                        print("Hi, fight been selected!")
                        screen.fill(pygame.Color("black"))
                        carryOn = False
                        moves_util.move_selection_option_player(screen, player_pokemon, opponent_pokemon, font, mouse_pos, carryOn, clock, move_bar, hp_bar, enemy_bar, player_pokemon_level, enemy_level, enemy_name, player_pokemon_name, player_pokemon_max_hp, background, player_sprite_back, opponent_sprite_front, opponent_background_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB, background, move_attack_bar, hp_bar, enemy_bar, what_will_you_do_textB, enemy_level, player_pokemon_level)
                    elif(player_pokemon.has_selected and not opponent_pokemon.has_selected):
                        print("Only the player has selected, waiting!")
                    elif(not player_pokemon.has_selected and opponent_pokemon.has_selected):
                        print("Only the opponent has selected, need from both!")
                """
                Fight check for both sides, due to player picking whichever after
                """
                if opponent_fight_rec.collidepoint(mouse_pos):
                    opponent_pokemon.has_selected = True
                    if(player_pokemon.has_selected and opponent_pokemon.has_selected):
                        print("Hi, fight been selected!")
                        screen.fill(pygame.Color("black"))
                        carryOn = False
                        moves_util.move_selection_option_player(screen, player_pokemon, opponent_pokemon, font, mouse_pos, carryOn, clock, move_bar, hp_bar, enemy_bar, player_pokemon_level, enemy_level, enemy_name, player_pokemon_name, player_pokemon_max_hp, background, player_sprite_back, opponent_sprite_front, opponent_background_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB, background, move_attack_bar, hp_bar, enemy_bar, what_will_you_do_textB, enemy_level, player_pokemon_level)
                    elif(player_pokemon.has_selected and not opponent_pokemon.has_selected):
                        print("Only the player has selected, waiting!")
                    elif(not player_pokemon.has_selected and opponent_pokemon.has_selected):
                        print("Only the opponent has selected, need from both!")
                elif bag_rect.collidepoint(mouse_pos):
                    print("Bag has been selected")

                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()              
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
