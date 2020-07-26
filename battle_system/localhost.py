import pygame
import os
import json
import glob
import random
from pathlib import Path
from pypresence import Presence
import time
from datetime import datetime
from pygame.locals import *
import sys

# Creates our colors
BLACK = (0, 0, 0)
transparent = (0, 0, 0, 0)
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

def render_pokemon_fainted(screen, background, player_sprite, move_bar, hp_bar, level_text,  Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp, move_text):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(level_text, (235, 124))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
    screen.blit(move_text,(8, 163))

def render2_status_screen(screen, background, icon1, icon2, icon3, icon4, icon5, icon6):
    screen.blit(background, (250,0))
    screen.blit(icon1, (255,0))
    screen.blit(icon2, (343,0))
    screen.blit(icon3, (430,0))
    screen.blit(icon4, (255,80))
    screen.blit(icon5, (343,80))
    screen.blit(icon6, (430,80))

def render1_attack_menu_bar(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp, move_text):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(level_text, (235, 124))
    screen.blit(enemy_level, (81, 32))
    screen.blit(enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
    screen.blit(move_text,(8, 163))

def render1_after_attack_physical(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
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
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))

def render_moves(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(level_text, (235, 124))
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))

def render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(enemy_level, (478, 124))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))

def render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(enemy_level, (478, 124))
    screenB.blit(FightB_option, (380, 165))
    screenB.blit(PokemonB_option, (380, 180))
    screenB.blit(BagB_option, (450, 165))
    screenB.blit(QuitB_option, (450, 180))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))
    
def render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(enemy_level, (478, 124))
    screenB.blit(FightB_option, (380, 165))
    screenB.blit(PokemonB_option, (380, 180))
    screenB.blit(BagB_option, (450, 165))
    screenB.blit(QuitB_option, (450, 180))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))

def render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
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
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))

# Does the status screen for the beginning
def status_screen_state(player, opponent, screen, background):
    player_icon1 = pygame.image.load(player.pokemon1.icon).convert_alpha()
    player_icon2 = pygame.image.load(player.pokemon2.icon).convert_alpha()
    player_icon3 = pygame.image.load(player.pokemon3.icon).convert_alpha()
    player_icon4 = pygame.image.load(player.pokemon4.icon).convert_alpha()
    player_icon5 = pygame.image.load(player.pokemon5.icon).convert_alpha()
    player_icon6 = pygame.image.load(player.pokemon6.icon).convert_alpha()

    enemy_icon1 = pygame.image.load(opponent.pokemon1.icon).convert_alpha()
    enemy_icon2 = pygame.image.load(opponent.pokemon2.icon).convert_alpha()
    enemy_icon3 = pygame.image.load(opponent.pokemon3.icon).convert_alpha()
    enemy_icon4 = pygame.image.load(opponent.pokemon4.icon).convert_alpha()
    enemy_icon5 = pygame.image.load(opponent.pokemon5.icon).convert_alpha()
    enemy_icon6 = pygame.image.load(opponent.pokemon6.icon).convert_alpha()

    screen.blit(background, (250,0))
    screen.blit(enemy_icon1, (255,0))
    screen.blit(enemy_icon2, (343,0))
    screen.blit(enemy_icon3, (430,0))
    screen.blit(enemy_icon4, (255,80))
    screen.blit(enemy_icon5, (343,80))
    screen.blit(enemy_icon6, (430,80))

    enemy_icon1_rect = Rect(255,0, 50, 50)
    enemy_icon2_rect = Rect(94,0, 50, 50)
    enemy_icon3_rect = Rect(180,0, 50, 50)
    enemy_icon4_rect = Rect(5,80, 50, 50)
    enemy_icon5_rect = Rect(94,80, 50, 50)
    enemy_icon6_rect = Rect(180,80, 50, 50)

    screen.blit(background, (0,0))
    screen.blit(player_icon1, (5,0))
    screen.blit(player_icon2, (94,0))
    screen.blit(player_icon3, (180,0))
    screen.blit(player_icon4, (5,80))
    screen.blit(player_icon5, (94,80))
    screen.blit(player_icon6, (180,80))

    player_icon1_rect = Rect(5,0, 50, 50)
    player_icon2_rect = Rect(94,0, 50, 50)
    player_icon3_rect = Rect(180,0, 50, 50)
    player_icon4_rect = Rect(5,80, 50, 50)
    player_icon5_rect = Rect(94,80, 50, 50)
    player_icon6_rect = Rect(180,80, 50, 50)
    carryOn = True
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            
        # --- Game logic should go here
        # Will be rewritten
            mouse_pos = pygame.mouse.get_pos()
            opponent_pos = pygame.mouse.get_pos()
            if pygame.key.get_pressed()[pygame.K_q]:
                print("The quit key has been used!")
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                Checks to see if we have no fainted pokemon, if we don't, add the pokemon to the list of current pokemon
                """
                if(len(player.pokemon_fainted) <= 0 and len(opponent.pokemon_fainted) <= 0):
                    """
                    Check if the mouse has clicked, and if we have any pokemons in our load out, if not, add pokemons. Only proceed if both players have pokemon
                    """
                    if(len(player.pokemon_in_use) <= 0):
                        if player_icon1_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon1)
                            print(player.pokemon1.name + " has joined the party!\nNow waiting for second player!\n")
                            
                        elif player_icon2_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon2)
                            print(player.pokemon2.name + " has joined the party!\nNow waiting for second player!\n")

                        elif player_icon3_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon3)
                            print(player.pokemon3.name + " has joined the party!\nNow waiting for second player!\n")

                    elif(len(opponent.pokemon_in_use) <= 0):
                        if(enemy_icon1_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon1)
                            print(opponent.pokemon1.name + " has joined the party!\nNow waiting for first player!\n")
                    else:
                        print("\nBoth players have confirmed their choices!")
                        print("Pokemon sent out are: " + str(player.pokemon_in_use[0].name) + " vs " + str(opponent.pokemon_in_use[0].name))
                        carryOn = False
                        pokemon_player_battle_state(player.pokemon_in_use[0], opponent.pokemon_in_use[0], screen)
                
                # else:
                #     for i in player.pokemon_defeated:
                #         if(i == "Pokemon1"):
                #             print("Pokemon1 is fainted, removing the option")
                #         elif(i == "Pokemon2"):
                #             print("hi")
                #         elif(i == "Pokemon3"):
                #             print("hi")
                #         elif(i == "Pokemon4"):
                #             print("hi")
                #         elif(i == "Pokemon5"):
                #             print("hi")
                #         elif(i == "Pokemon6"):
                #             print("hi")
                #     for i in opponent.pokemon_defeated:
                #         if(i == "Pokemon1"):
                #             print("Pokemon1 is fainted, removing the option")
                #         elif(i == "Pokemon2"):
                #             print("hi")
                #         elif(i == "Pokemon3"):
                #             print("hi")
                #         elif(i == "Pokemon4"):
                #             print("hi")
                #         elif(i == "Pokemon5"):
                #             print("hi")
                #         elif(i == "Pokemon6"):
                #             print("hi"
                
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

# Does all of our move logic
def local_host_move_logic(move_name, player_pokemon, opponent_pokemon, screen, background,  move_attack_bar, hp_bar, enemy_bar,  level_text, enemy_Level, move_text, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB):
    with open("battle_system/move_data/" + move_name + ".json", "r") as loop:
                move = json.load(loop)
                        
    damage = move["Data"]["Base_Damage"]
    status = move["Data"]["Status"]
    # Checks if we have a damage hitting move
    if(status == "Damage"):
        # Checks if have any health
        if(enemy_current_health > 0):
        # Take away the enemy's health
            enemy_current_health -= damage
            screen.fill(pygame.Color("black")) # erases the entire screen surface
            pokemon_current_hp = font.render(str(current_health), True, BLACK)
            move_text = font.render(player_pokemon + " attacks "+ opponent_pokemon + " with " + move_name + " dealing " + str(damage) + " damage", True, BLACK)
            render1_attack_menu_bar(screen, background, player_sprite, enemy_sprite, move_attack_bar, hp_bar, enemy_bar,  level_text, enemy_Level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp, move_text)
            enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
            what_will_you_do_textB = font.render(opponent_pokemon[0] + " was dealt " + str(damage) + " damage from " + player_pokemon[0] + "'s " + move_name, True, BLACK)
            render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, move_attack_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                
            screenB.fill(pygame.Color("black"))
            what_will_you_do_textB = font.render("What will " + opponent.pokemon + " do?", True, BLACK)
            render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, fight_option, pokemon_option, bag_option, quit_option, enemy_Level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp)
            render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)

            if(enemy_current_health <= 0):
                screenB.fill(pygame.Color("black")) # erases the entire screen surface
                enemy_current_health = 0
                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                move_text = font.render(opponent_pokemon + " has fainted! Now awaiting for next pokemon", True, BLACK)
                render_pokemon_fainted(screen, background, player_sprite, move_attack_bar, hp_bar, level_text,  player_pokemon_name, pokemon_max_hp, pokemon_current_hp, move_text)
                # Keeps track of the pokemon who has fainted
                opponent_pokemon.fainted.append(opponent_pokemon)
                render2_status_screen(screenB, status_screen, enemy_icon1, enemy_icon2, enemy_icon3, enemy_icon4, enemy_icon5, enemy_icon6)
                print(opponent_pokemon + " has fainted!")
            if(status == "Status-effect"):
                print(move_name + " causes a status, no damage taken!")

# Loads our menu whenever we click fight on the player side
def move_selection_option_player(screen, num_of_pokemon, font, mouse_pos):
    move_1 = font.render(num_of_pokemon[1],True, BLACK)
    screen.blit(move_1, (4,165))
    move_2 = font.render(num_of_pokemon[2],True, BLACK)
    screen.blit(move_2, (4,180))
    move_3 = font.render(num_of_pokemon[3],True, BLACK)
    screen.blit(move_3, (65,165))
    move_4 = font.render(num_of_pokemon[4],True, BLACK)
    screen.blit(move_4, (65,180))
    # Player's moves
    move1_rect1 = Rect(4,165, 50, 50)
    move2_rect1 = Rect(4,180, 50, 50)
    move3_rect1 = Rect(65,165, 50, 50)
    move4_rect1 = Rect(65,180, 50, 50)

    if move1_rect1.collidepoint(mouse_pos):
        print(num_of_pokemon[1] + "is currently being used!")
"""
Removes everything but the name of the background
"""
def background_trimmer(background):
    trim = background.replace("battle_system/battle_code/resources/graphics/battle_backgrounds/", "")
    trim = trim.replace(".png", "")
    trim = trim[:1].upper() + trim[1:]
    return trim

def pokemon_player_battle_state(player_pokemon, opponent_pokemon, screen):
    clock = pygame.time.Clock()
    now = datetime.now()
    current_time = now.strftime("%H")
    """
    Uses time and determines what background it will be based on keywords
    """
    if int(current_time) >= 18  or int(current_time) >= 1 and int(current_time) < 7:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "Night")
    if int(current_time) >= 7 and int(current_time) <= 11:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "Morning")
    if int(current_time) >= 12 and int(current_time) <= 17:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "Afternoon")
    background_stand_alone = background_trimmer(background)
    with open("battle_system/pokemon_data/" + player_pokemon.name + ".json", "r") as loop:
            player_data = json.load(loop)

    with open("battle_system/pokemon_data/" + opponent_pokemon.name + ".json", "r") as loop:
            opponent_data = json.load(loop)

    player_background_front_x = player_data["Front_Position"][background_stand_alone + "_X_Pos"]
    player_background_front_y = player_data["Front_Position"][background_stand_alone + "_Y_Pos"]
    player_background_back_x = player_data["Back_Position"][background_stand_alone + "_X_Pos"]
    player_background_back_y = player_data["Back_Position"][background_stand_alone + "_Y_Pos"]

    opponent_background_front_x = opponent_data["Front_Position"][background_stand_alone + "_X_Pos"]
    opponent_background_front_y = opponent_data["Front_Position"][background_stand_alone + "_Y_Pos"]
    opponent_background_back_x = opponent_data["Back_Position"][background_stand_alone + "_X_Pos"]
    opponent_background_back_y = opponent_data["Back_Position"][background_stand_alone + "_Y_Pos"]

    background = pygame.image.load(background).convert_alpha()
    system_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/system_bar.png").convert_alpha()
    hp_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
    enemy_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
    move_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/move_bar.png").convert_alpha()
    move_attack_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/attack_bar.png").convert_alpha()
    font = pygame.font.SysFont('arial', 10)
    fight_option = font.render("FIGHT", True, BLACK)
    pokemon_option = font.render("POKEéMON", True, BLACK)
    bag_option = font.render("BAG", True, BLACK)
    quit_option = font.render("QUIT", True, BLACK)
    enemy_name = font.render(opponent_pokemon.name, True, BLACK)
    player_pokemon_name = font.render(player_pokemon.name, True, BLACK)
    player_pokemon_max_hp = font.render(str(player_pokemon.HP), True, BLACK)
    what_will_you_do = font.render("What will " + player_pokemon.name + " do?", True, BLACK)
    player_pokemon_level = font.render(str(player_pokemon.level), True, BLACK)
    fight_rec = Rect(130, 165, 20, 10)
    pokemon_rect = Rect(130, 180, 20, 10)
    bag_rect = Rect(195, 165, 20, 10)
    quit_rect = Rect(195, 180, 20, 10)

    player_sprite_back = pygame.image.load(player_pokemon.back)
    opponent_sprite_front = pygame.image.load(opponent_pokemon.front)
    screen.blit(background, (0,0))
    screen.blit(background, (250, 0))
    screen.blit(player_sprite_back, (player_background_back_x,(player_background_back_y + 110)))
    # screen.blit(opponent_sprite_front, (150,50))
    screen.blit(opponent_sprite_front, ((150 + opponent_background_front_x),(50 + opponent_background_front_y)))
    screen.blit(system_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do, (8, 163))
    screen.blit(player_pokemon_level, (205, 124))
    screen.blit(fight_option, (130, 165))
    screen.blit(pokemon_option, (130, 180))
    screen.blit(bag_option, (195, 165))
    screen.blit(quit_option, (195, 180))
    # screen.blit(enemy_level, (81, 32))
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
                if fight_rec.collidepoint(mouse_pos):
                    print("Hi, fight been selected!")
                    #screen.fill(pygame.Color("black"))
                    #render_moves(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp)
                    #move_selection_option_player(screen, player.pokemon1, font, mouse_pos)
                    
                elif bag_rect.collidepoint(mouse_pos):
                    print("Bag has been selected")

                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()              
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
# Loads in our basic assets that will be loaded each fight
def start_game(player, opponent):
    pygame.init()
    with open("battle_system/battle_code/config/game_config.json", "r") as loop:
                gameconfig = json.load(loop)
    
    width = gameconfig["Resolution"]["Width"]
    height = gameconfig["Resolution"]["Height"]
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pokemon Battle Sim")
    screenB = pygame.display.set_mode((500,195), 0, 32)

    # now = datetime.now()
    # current_time = now.strftime("%H")
    # # Start with status screen on both sides to get pokemon data and pass it in
    # if int(current_time) >= 18  or int(current_time) >= 1 and int(current_time) < 7:
    #     background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "night")
    # if int(current_time) >= 7 and int(current_time) <= 11:
    #     background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "morning")
    # if int(current_time) >= 12 and int(current_time) <= 17:
    #     background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "afternoon")

    # background = pygame.image.load(background).convert_alpha()
    # system_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/system_bar.png").convert_alpha()
    # hp_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
    # enemy_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
    # move_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/move_bar.png").convert_alpha()
    # move_attack_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/attack_bar.png").convert_alpha()
    music_string = select_music('battle_system/battle_code/resources/music/')
    pygame.mixer.music.load(music_string)
    pygame.mixer.music.play(-1)
    status_screen = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/status_screen.png").convert_alpha()
    status_screen_state(player, opponent, screen, status_screen)
    # font = pygame.font.SysFont('arial', 12)
    # fight_option = font.render("FIGHT", True, BLACK)
    # pokemon_option = font.render("POKEéMON", True, BLACK)
    # bag_option = font.render("BAG", True, BLACK)
    # quit_option = font.render("QUIT", True, BLACK)
    # fight_rec1 = Rect(130, 165, 20, 10)
    # pokemon_rect1 = Rect(130, 180, 20, 10)
    # bag_rect1 = Rect(195, 165, 20, 10)
    # quit_rect1 = Rect(195, 180, 20, 10)
    
    # render1_screen(screen, background, player.pokemon1.back, opponent.pokemon1.front, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, fight_option, pokemon_option, bag_option, quit_option, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp)
    # fight_rec1 = Rect(130, 165, 20, 10)
    # pokemon_rect1 = Rect(130, 180, 20, 10)
    # bag_rect1 = Rect(195, 165, 20, 10)
    # quit_rect1 = Rect(195, 180, 20, 10)
    
    
    
    # # Begins the second window
    # fightB_option = font.render("FIGHT", True, BLACK)
    # pokemonB_option = font.render("POKEéMON", True, BLACK)
    # bagB_option = font.render("BAG", True, BLACK)
    # quitB_option = font.render("QUIT", True, BLACK)
    # fight_rec2 = Rect(380, 165, 20, 10)
    # pokemon_rect2 = Rect(380, 180, 20, 10)
    # bag_rect2 = Rect(450, 165, 20, 10)
    # quit_rect2 = Rect(450, 180, 20, 10)

    # render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)
    
    # # The loop will carry on until the user exit the game (e.g. clicks the close button).
    # carryOn = True
    # isPokemon1 = True
    # # The clock will be used to control how fast the screen updates
    # clock = pygame.time.Clock()
 
    # # -------- Main Program Loop -----------
    # while carryOn:
    # # --- Main event loop
    #     for event in pygame.event.get(): # User did something
    #         if event.type == pygame.QUIT: # If user clicked close
    #             carryOn = False # Flag that we are done so we exit this loop
            
    #     # --- Game logic should go here
    #     # Will be rewritten
    #         mouse_pos = pygame.mouse.get_pos()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if fight_rec1.collidepoint(mouse_pos):
    #                 print("Hi, fight been selected!")
    #                 screen.fill(pygame.Color("black"))
    #                 render_moves(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp)
    #                 move_selection_option_player(screen, player.pokemon1, font, mouse_pos)
                    
    #             elif bag_rect1.collidepoint(mouse_pos):
    #                 print("Bag has been selected")

    #             elif quit_rect1.collidepoint(mouse_pos):
    #                 pygame.quit()
    #                 sys.exit()
    #             elif fight_rec2.collidepoint(mouse_pos):
    #                 print("Hi, fight been selected on the otherside!")
    #                 screen.fill(pygame.Color("black"))
    #                 render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)
    #                 # Enemey moves moves
    #                 # move1_rect2 = Rect(4,165, 50, 50)
    #                 # move2_rect2 = Rect(4,180, 50, 50)
    #                 # move3_rect2 = Rect(65,165, 50, 50)
    #                 # move4_rect2 = Rect(65,180, 50, 50)

                    

    #             elif bag_rect2.collidepoint(mouse_pos):
    #                 print("Bag has been selected")

    #             elif quit_rect2.collidepoint(mouse_pos):
    #                 pygame.quit()
    #                 sys.exit()         
                    
    #     # --- Go ahead and update the screen with what we've drawn.
    #     pygame.display.flip()
     
    #     # --- Limit to 60 frames per second
    #     clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()