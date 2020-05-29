# import pygame
# import os
# import json
# import glob
# import random
# from pathlib import Path
# from pypresence import Presence
# import time
# from datetime import datetime
# damage = 0
# # Uses primarily for rendering the player screen 
# def render_screen(player, opponent, num_of_pokemon, num_of_move, pokemon_currently_out, background):
#     # Loads all the assets that are needed for the updates
#     system_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/system_bar.png").convert_alpha()
#     hp_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
#     enemy_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
#     arrow = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/arrow.png").convert_alpha()
#     move_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/move_bar.png").convert_alpha()
#     move_attack_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/attack_bar.png").convert_alpha()
#     status_screen = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/status_screen.png").convert_alpha()
#     font = pygame.font.SysFont(None, 12)
#     what_will_you_do_text = font.render("What will " + player.pokemon1[0] + " do?", True, BLACK)
#     level_text = font.render(str(player.pokemon1[5]), True, BLACK)
#     fight_option = font.render("FIGHT", True, BLACK)
#     fight_rec = Fight_option.get_rect()
#     pokemon_option = font.render("POKEéMON", True, BLACK)
#     bag_option = font.render("BAG", True, BLACK)
#     quit_option = font.render("QUIT", True, BLACK)
#     enemy_Level = font.render(str(opponent.pokemon + num_of_pokemon + [5]), True, BLACK)
#     enemy_name = font.render(str(opponent.pokemon1[0]), True, BLACK)
#     player_pokemon_name = font.render(str(player.pokemon + num_of_pokemon[0]), True, BLACK)
#     pokemon_max_hp = font.render(str(player.pokemon + num_of_pokemon[7]), True, BLACK)
#     pokemon_current_hp = font.render(str(player.pokemon + num_of_pokemon[7]), True, BLACK)
#     move + num_of_move = player.pokemon + num_of_pokemon + [1]
#     with open("battle_system/move_data/" + move + num_of_move + ".json", "r") as loop:
#                 move1 = json.load(loop)
                        
#     damage = move + num_of_move["Data"]["Base_Damage"]
#     status = move + num_of_move["Data"]["Status"]
#     # Checks if we have a damage hitting move
#     if(status == "Damage"):
#         # Checks if have any health
#         if(enemy_current_health > 0):
#         # Take away the enemy's health
#             enemy_current_health -= damage
#             screen.fill(pygame.Color("black")) # erases the entire screen surface
#             pokemon1_current_hp = font.render(str(current_health), True, BLACK)
#             move_text = font.render(player.pokemon_currently_out + " attacks "+ opponent.pokemon_currently_out[0] + " with " + move + num_of_move " dealing " +str(damage) + " damage", True, BLACK)
#             render1_attack_menu_bar(screen, background, player_sprite, enemy_sprite, move_attack_bar, hp_bar, enemy_bar,  level_text, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp, move_text)
#             enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
#             what_will_you_do_textB = font.render(opponent.pokemon_currently_out[0] + " was dealt " + str(damage) + " damage from " + player.pokemon_currently_out[0] + "'s " + Move1, True, BLACK)
#             render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, move_attack_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                
#             screenB.fill(pygame.Color("black"))
#             what_will_you_do_textB = font.render("What will " + opponent.pokemon_currently_out[0] + " do?", True, BLACK)
#             render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, Enemy_Level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
#             render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)

#             if(enemy_current_health <= 0):
#                 screenB.fill(pygame.Color("black")) # erases the entire screen surface
#                 enemy_current_health = 0
#                 enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
#                 move_text = font.render(opponent.pokemon_currently_out[0] + " has fainted! Now awaiting for next pokemon", True, BLACK)
#                 render_pokemon_fainted(screen, background, player_sprite, move_attack_bar, hp_bar, level_text,  Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp, move_text)
#                 # Keeps track of the pokemon who has fainted
#                 fainted = pokemon_currently_out
#                 render2_status_screen(screenB, status_screen, enemy_icon1, enemy_icon2, enemy_icon3, enemy_icon4, enemy_icon5, enemy_icon6)
#                 print(opponent.pokemon1[0] + " has fainted!")
#             if(status == "Status-effect"):
#                 print(move + num_of_move + " causes a status, no damage taken!")
                
            